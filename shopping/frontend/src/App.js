import React, { Component } from 'react';
import './App.css';
import CardList from './components/card-list/card-list.component';
import Header from './components/header/header.js';
import SearchBox from './components/search-box/search-box.component.jsx';
import productsData from './product_list.json';
import api from "./utils/Api.js";
import { Routes, Route } from 'react-router-dom';

class App extends Component {
  constructor() {
    super();
    this.state = {
      searchField: '',
      products: productsData,
      fav: new Set(),
      cart: [],
      cartSet: new Set(),
      tab: 1, // 1=main; 2=fvrt; 3=cart
      analysedCosts: 0,
      analysedCart: [],
      analysedCartSet: new Set()
    };
  }

  componentDidMount() {
    this.getAllProducts();
  }

  getAllProducts() {
    api.getAllProducts()
      .then((initialProducts) => {
        if (initialProducts !== undefined) {
          this.setState({ products: initialProducts });
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }

  totalPrice = () => {
    const { cart } = this.state;
    return (cart.reduce((total, item) => (total + parseFloat(item.price.replace(',', '.'))), 0).toFixed(2).replace('.', ','));
  }

  handleToggleFav = (product) => {
    const { fav } = this.state;
    const newFav = new Set(fav);
    if (fav.has(product)) {
      newFav.delete(product);
    } else {
      newFav.add(product);
    }
    this.setState({ fav: newFav });
  };

  handleAddToCart = (product) => {
    this.setState(prevState => ({
      cart: [...prevState.cart, product]
    }), () => {
      this.changeCartSet();
    });
  }

  handleRemoveFromCart = (product) => {
    const index = this.state.cart.indexOf(product);
    if (index !== -1) {
      const updatedCart = [
        ...this.state.cart.slice(0, index),
        ...this.state.cart.slice(index + 1)
      ];
      this.setState({
        cart: updatedCart
      }, () => {
        this.changeCartSet();
      });
    }
  }

  changeCartSet = () => {
    const { cart } = this.state;
    const newCartSet = new Set(cart);
    const k = this.totalPrice(cart);
    this.setState({
      cartSet: newCartSet,
      analysedCosts: "Цена без доставки, без оптимизации " + k + " ₽"
    });
  }

  cartCount = (product) => {
    const { cart } = this.state;
    return cart.filter(item => item === product).length;
  }

  switchTab = (num) => {
    this.setState({ searchField: "" });
    this.setState({ tab: num });
  }

  analysedCartCount = (product) => {
    const { analysedCart } = this.state;
    return analysedCart.filter(item => item === product).length;
  }

  confirmCart = () => {
    const cartJSON = JSON.stringify(this.state.cart);
    this.getAnalysedCosts(cartJSON);
  }

  getAnalysedCosts(cart) {
    api.getAnalysedCost(cart)
      .then((resultString) => {
        let jsonString = resultString.replace(/'/g, '"');
        try {
          const result = JSON.parse(jsonString);
          this.setState({
            analysedCart: result[1],
            analysedCosts: "Оптимизированная цена с доставкой " + result[0],
            analysedCartSet: new Set(result[1])
          });
        } catch {
          this.setState({ analysedCosts: jsonString });
        }
      });
  }

  onSearchChange = (event) => {
    const searchField = event.target.value.toLowerCase();
    this.setState({ searchField });
  };

  renderContent() {
    const { products, searchField, analysedCosts, cart, cartSet, fav, analysedCartSet } = this.state;
    const { onSearchChange } = this;
    const filteredProducts = products.filter((product) => product.name.toLowerCase().includes(searchField));

    return (
      <div className="App">
        <div className='page'>
          <Header />
          <Routes>
            <Route path="/" element={
              <div>
                <SearchBox
                  className='products-search-box'
                  onChangeHandler={onSearchChange}
                  placeholder='Поиск'
                />
                <hr />
                <CardList
                  products={filteredProducts}
                  onAddToCart={this.handleAddToCart}
                  onRemoveFromCart={this.handleRemoveFromCart}
                  onToggleFav={this.handleToggleFav}
                  cartCount={this.cartCount}
                />
              </div>
            } />

            <Route path="/fav" element={
              <div>
                <hr />
                <CardList
                  products={[...fav]}
                  onAddToCart={this.handleAddToCart}
                  onRemoveFromCart={this.handleRemoveFromCart}
                  onToggleFav={this.handleToggleFav}
                  cartCount={this.cartCount}
                />
              </div>
            } />

            <Route path="/cart" element={
              <div>
                <hr />
                {[...cartSet].map((product) => (
                  <div key={product.id}>
                    <div>
                      <h3>
                        {product.name} <button className="button button_type_small" onClick={() => this.handleToggleFav(product)}>♡</button>
                      </h3>
                    </div>
                    <div>{product.store}: {product.price}₽</div>
                    <div>
                      <button className="button button_type_small" onClick={() => this.handleRemoveFromCart(product)}>-</button>
                      {" " + this.cartCount(product) + " "}
                      <button className="button button_type_small" onClick={() => this.handleAddToCart(product)}>+</button>
                    </div>
                    <hr />
                  </div>
                ))}
                <h2>{analysedCosts}</h2>
                <hr />
                <button className="button button_type_main" onClick={this.confirmCart}>Подтвердить</button>
                {[...analysedCartSet].map((product) => (
                  <div key={product.id}>
                    <div>{product.name}: {this.analysedCartCount(product)}</div>
                    <div>{product.store}: {product.price}₽</div>
                    <hr />
                  </div>
                ))}
              </div>
            } />
          </Routes>
        </div>
      </div>
    );
  }

  render() {
    return (
      <div>
        {this.renderContent()}
      </div>
    );
  }
}

export default App;

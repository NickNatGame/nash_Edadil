import React, { Component } from 'react';
import './App.css';
import CardList from './components/card-list/card-list.component';
import Header from './components/header/header.js';
import SearchBox from './components/search-box/search-box.component.jsx';
import productsData from './product_list.json';
import api from "./utils/Api.js"

import { Routes, Route} from 'react-router-dom';

class App extends Component {
  constructor() {
    super();
    this.state = {
      searchField: '',
      products: productsData,
      fav: new Set(),
      cart: [],
      cartSet: new Set(),
      tab: 1, // 1=main; 2=fvrt; 3;cart
      analysedCosts: 0
    };
  }

  getAllProducts() {
    api.getAllProducts()
   .then((initialProducts) => {
      if (initialProducts!== undefined) {
        this.setState({products: initialProducts})
      }

    })
   .catch((err) => {
      console.log(err);

    })
  }

  handleToggleFav = (product) => {
    const { fav } = this.state;
    if (fav.has(product)) {
      const newFav = new Set(fav);
      newFav.delete(product);
      this.setState({ fav: newFav });
    }
    else {
      const newFav = new Set(fav);
      newFav.add(product);
      this.setState({ fav: newFav });
    }
  };

  handleAddToCart = (product) => {
    this.setState({
      cart: [...this.state.cart, product]
    }, () => {
      this.changeCartSet();
    });
  }

  handleRemoveFromCart = (product) => {
    const index = this.state.cart.indexOf(product);
    if (index!== -1) {
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
    this.setState({ cartSet: newCartSet });
  }

  cartCount = (product) => {
    const { cart } = this.state;
    let count = 0;
    cart.forEach(item => {
        if (item === product) {
            count++;
        }
    });
    return count;
  }

  switchTab = (num) =>{
    this.setState({searchField:""});
    this.setState({tab:num});
  }

  confirmCart = () => {
    var cartJSON = JSON.stringify(this.state.cart);
    this.getAnalysedCosts(cartJSON);
  }
  getAnalysedCosts(cart)
  {
    api.getAnalysedCost(cart)
    .then((result) => {this.setState({analysedCosts: String(result).replace("[","").replace("]","")});})
  }


  onSearchChange=(event)=>{
    const searchField = event.target.value.toLowerCase();
    this.setState(()=>{
      return {searchField};
    });
  };

  renderContent() {
    const { products, searchField, analysedCosts } = this.state;
    const {onSearchChange} =this;
    const filteredProducts = products.filter((product) => {
      return product.name.toLowerCase().includes(searchField);
    });

    return (
      <div className="App">
        <div className='page'>
          <Header/>
          <Routes>
            <Route path="/" element = {
              <div>
              <SearchBox
                className='products-search-box'
                onChangeHandler={onSearchChange}
                placeholder='Поиск'
              />
              <hr />
              <CardList products={filteredProducts} onAddToCart={this.handleAddToCart} onRemoveFromCart={this.handleRemoveFromCart} onToggleFav={this.handleToggleFav} cartCount={this.cartCount}/>
            </div>
            }
            />

            <Route path="/fav" element = {
                  <div>
                  <hr />
                  <CardList products={[...this.state.fav]} onAddToCart={this.handleAddToCart} onRemoveFromCart={this.handleRemoveFromCart} onToggleFav={this.handleToggleFav} cartCount={this.cartCount}/>
                </div>
            }/>

            <Route path="/cart" element = {
              <div>
              <hr />
              {[...this.state.cartSet].map((product) => (
                <div key={product.id}>
                  <div><h3>{product.name} <button className="button button_type_small" onClick={() => this.handleToggleFav(product)}>♡</button></h3></div>
                  <div>{product.store}: {product.price}₽</div>
                    <div>
                      <button className="button button_type_small" onClick={() => this.handleRemoveFromCart(product)}>-</button>
                      {"    "+this.cartCount(product)+"   "}
                      <button className="button button_type_small" onClick={() => this.handleAddToCart(product)}>+</button>
                    </div>
                  <div>{this.cartCount}</div>
                  <hr />
                </div>
              ))}
              <h2>{analysedCosts}</h2>
              <hr />
              <button className="button button_type_main" onClick={()=>this.confirmCart()}>Подтвердить</button>
            </div>
            }/>
          </Routes>
        </div>
      </div>
    );
  }

  render() {
    return (
      <div >
        {this.renderContent()}
      </div>
    );
  }
}

export default App;

import React, { Component } from 'react';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import CardList from './components/card-list/card-list.component';
import Header from './components/header/header';
import SearchBox from './components/search-box/search-box.component';
import productsData from './product_list.json';
import api from './utils/Api';

class App extends Component {
  constructor() {
    super();
    this.state = {
      searchField: '',
      products: productsData,
      fav: new Set(),
      cart: [],
      cartSet: new Set(),
<<<<<<< Updated upstream
      tab: 1, // 1=main; 2=fvrt; 3=cart
      analysedCosts: 0,
=======
      analysedCosts: '',
>>>>>>> Stashed changes
      analysedCart: []
    };
  }

  componentDidMount() {
    this.getAllProducts();
  }

  getProductKey = (product) => `${product.name}-${product.store}-${product.price}`;

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
    return cart
      .reduce((total, item) => (total + parseFloat(item.price.replace(',', '.'))), 0)
      .toFixed(2)
      .replace('.', ',');
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
    const k = this.totalPrice();
    this.setState({
      cartSet: newCartSet,
      analysedCosts: `Цена без доставки, без оптимизации ${k} ₽`
    });
  }

  cartCount = (product) => {
    const { cart } = this.state;
    return cart.filter(item => item === product).length;
  }

  confirmCart = () => {
<<<<<<< Updated upstream
=======
    if (this.state.cart.length === 0) {
      this.setState({
        analysedCosts: 'Корзина пуста',
        analysedCart: []
      });
      return;
    }
>>>>>>> Stashed changes
    const cartJSON = JSON.stringify(this.state.cart);
    this.getAnalysedCosts(cartJSON);
  }

  getAnalysedCosts(cart) {
    api.getAnalysedCost(cart)
      .then((result) => {
        if (result.ok) {
          this.setState({
<<<<<<< Updated upstream
            analysedCart: result[1],
            analysedCosts: "Оптимизированная цена с доставкой " + result[0]
=======
            analysedCart: result.items || [],
            analysedCosts: `Оптимизированная цена с доставкой ${result.message}`
>>>>>>> Stashed changes
          });
          console.log(result[1]);
        } catch {
          this.setState({ analysedCosts: jsonString });
        }
<<<<<<< Updated upstream
=======

        this.setState({
          analysedCart: [],
          analysedCosts: result.message || 'Не удалось оптимизировать корзину'
        });
      })
      .catch((err) => {
        this.setState({
          analysedCart: [],
          analysedCosts: `Ошибка при анализе корзины: ${err}`
        });
>>>>>>> Stashed changes
      });
  }

  onSearchChange = (event) => {
    const searchField = event.target.value.toLowerCase();
    this.setState({ searchField });
  };

  renderMainPage = () => {
    const { products, searchField } = this.state;
    const filteredProducts = products.filter((product) => product.name.toLowerCase().includes(searchField));

    return (
<<<<<<< Updated upstream
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
                  <div key={`${product.name}-${product.store}`}>
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
                {analysedCart.map((product, index) => (
                  <div key={index}>
                    <div>{product.name}</div>
                    <div>{product.store}: {product.price}₽</div>
                    <hr />
                  </div>
                ))}
              </div>
            } />
          </Routes>
=======
      <section className="content-section" aria-label="Каталог товаров">
        <div className="search-row">
          <SearchBox
            className="products-search-box"
            onChangeHandler={this.onSearchChange}
            placeholder="Поиск по названию"
          />
>>>>>>> Stashed changes
        </div>
        <CardList
          products={filteredProducts}
          onAddToCart={this.handleAddToCart}
          onRemoveFromCart={this.handleRemoveFromCart}
          onToggleFav={this.handleToggleFav}
          cartCount={this.cartCount}
        />
      </section>
    );
  }

  renderFavPage = () => {
    const { fav } = this.state;
    const favProducts = [...fav];

    return (
      <section className="content-section" aria-label="Избранные товары">
        {favProducts.length === 0 ? (
          <p className="empty-state">В избранном пока нет товаров</p>
        ) : (
          <CardList
            products={favProducts}
            onAddToCart={this.handleAddToCart}
            onRemoveFromCart={this.handleRemoveFromCart}
            onToggleFav={this.handleToggleFav}
            cartCount={this.cartCount}
          />
        )}
      </section>
    );
  }

  renderCartItem = (product) => (
    <article className="cart-item" key={this.getProductKey(product)}>
      <div className="cart-item__main">
        <h3>{product.name}</h3>
        <button className="button button_type_small" onClick={() => this.handleToggleFav(product)}>♡</button>
      </div>
      <p className="cart-item__price">{product.store}: {product.price} ₽</p>
      <div className="cart-item__controls">
        <button className="button button_type_small" onClick={() => this.handleRemoveFromCart(product)}>-</button>
        <span>{this.cartCount(product)}</span>
        <button className="button button_type_small" onClick={() => this.handleAddToCart(product)}>+</button>
      </div>
    </article>
  )

  renderOptimizedItem = (product, index) => (
    <article className="optimized-item" key={`${this.getProductKey(product)}-${index}`}>
      <p>{product.name}</p>
      <p>{product.store}: {product.price} ₽</p>
    </article>
  )

  renderCartPage = () => {
    const { analysedCosts, cartSet, analysedCart } = this.state;
    const cartItems = [...cartSet];

    return (
      <section className="content-section" aria-label="Корзина">
        {cartItems.length === 0 ? (
          <p className="empty-state">Корзина пуста</p>
        ) : (
          <div className="cart-list">{cartItems.map(this.renderCartItem)}</div>
        )}

        <div className="cart-summary">
          <h2>{analysedCosts || 'Добавьте товары для расчета'}</h2>
          <button className="button button_type_main" onClick={this.confirmCart}>Подтвердить</button>
        </div>

        {analysedCart.length > 0 && (
          <div className="optimized-list" aria-label="Оптимизированная корзина">
            {analysedCart.map(this.renderOptimizedItem)}
          </div>
        )}
      </section>
    );
  }

  render() {
    return (
      <div className="app-shell">
        <div className="page">
          <Header />
          <main>
            <Routes>
              <Route path="/" element={this.renderMainPage()} />
              <Route path="/fav" element={this.renderFavPage()} />
              <Route path="/cart" element={this.renderCartPage()} />
            </Routes>
          </main>
        </div>
      </div>
    );
  }
}

export default App;

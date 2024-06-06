import React, { Component } from 'react';
import './App.css';
import CardList from './components/card-list/card-list.component';
import SearchBox from './components/search-box/search-box.component.jsx';
import productsData from './product_list.json';

class App extends Component {
  constructor() {
    super();
    this.state = {
      searchField: '',
      products: productsData,
      fav: new Set(),
      cart: [],
      cartSet: new Set(),
      tab: 1 // 1=main; 2=fvrt; 3;cart
    };
  }

  handleToggleFav = (product) => { //добавить в/убрать из изб.
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
    //console.log("Updated fav:", this.state.fav);
  };

  handleAddToCart = (product) => { //добавить в cart
    this.setState({
      cart: [...this.state.cart, product]
    }, () => {
      this.changeCartSet();
      //console.log('Updated cart:', this.state.cart);
    });
  }

  handleRemoveFromCart = (product) => { //удалить из cart
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
        //console.log('Updated Cart Array:', this.state.cart);
      });
    }
  }
  
  changeCartSet = () => { //обновить cartSet в соответствии с cart
    const { cart } = this.state;
    const newCartSet = new Set(cart);
    this.setState({ cartSet: newCartSet }, () => {
      //console.log('Updated Cart Set:', this.state.cartSet);
    });
  }

  cartCount = (product) => { //кол-во вхождений product в cart
    const { cart } = this.state;
    let count = 0;
    cart.forEach(item => {
        if (item === product) {
            count++;
        }
    });
    return count;
  }

  switchTab = (num) =>{ //поменять вкладку
    this.setState({searchField:""});
    this.setState({tab:num});
  }

  confirmCart = () => { //подтведить корзину, записать .json ?
    var cartJSON = JSON.stringify(this.state.cart);
    console.log(cartJSON);
  }

  onSearchChange=(event)=>{
    const searchField = event.target.value.toLowerCase();
    this.setState(()=>{
      return {searchField};
    });
  };

  
  renderContent() {

    const { tab, products, searchField } = this.state;
    const {onSearchChange} =this;
    
    const filteredProducts = products.filter((product) => { //фильтр по строке поиска
      return product.name.toLowerCase().includes(searchField);
    });

    const totalPrice = () => { //общая стоимость
      const { cart } = this.state;
      return (cart.reduce((total, item) => (total + parseFloat(item.price.replace(',', '.'))), 0).toFixed(2).replace('.', ','));
    }



    return (
      <div className="App">
        <div>
          <button onClick={() => this.switchTab(1)} style={{ marginRight: '10px' }}>Все товары</button>
          <button onClick={() => this.switchTab(2)} style={{ marginRight: '10px' }}>Избранное</button>
          <button onClick={() => this.switchTab(3)} style={{ marginRight: '10px' }}>Корзина</button>
        </div>
        
  
        {tab === 1 && (                   //все = filteredProducts
          <div>
            <SearchBox 
              className='products-search-box'
              onChangeHandler={onSearchChange} 
              placeholder='Поиск'
              
            />
            <hr />
            <CardList products={filteredProducts} onAddToCart={this.handleAddToCart} onRemoveFromCart={this.handleRemoveFromCart} onToggleFav={this.handleToggleFav} cartCount={this.cartCount}/>
          </div>
          )
        }
  
        {tab === 2 && (                 //избранное = fav [...this.state.fav]
          <div>
            <hr />
            <CardList products={[...this.state.fav]} onAddToCart={this.handleAddToCart} onRemoveFromCart={this.handleRemoveFromCart} onToggleFav={this.handleToggleFav} cartCount={this.cartCount}/>
          </div>
        )}
        {tab === 3 && (
        <div>
          <hr />
          {[...this.state.cartSet].map((product) => (
            <div key={product.id}>
              <div><h3>{product.name} <button onClick={() => this.handleToggleFav(product)}>♡</button></h3></div>
              <div>{product.store}: {product.price}₽</div>
                <div>
                  <button onClick={() => this.handleRemoveFromCart(product)}>-</button> 
                  {"    "+this.cartCount(product)+"   "}
                  <button onClick={() => this.handleAddToCart(product)}>+</button> 
                </div>
              <div>{this.cartCount}</div> 
              <hr />
            </div>
          ))}
          <h2>{totalPrice()} ₽</h2>
          <hr />
          <button onClick={()=>this.confirmCart()}> C:</button>
        </div>
      )}
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
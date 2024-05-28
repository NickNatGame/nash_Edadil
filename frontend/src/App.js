import './App.css';
import { Component } from 'react';

class App extends Component {
  constructor(){
    super();
    this.state={
      searchField:'',
      products:  [
        {
          "name": "Яблоки 1кг",
          "price": 50,
          "image": null,
          "store": "Пятёрочка",
        },
        {
          "name": "Хлеб белый",
          "price": 30,
          "image": null,
          "store": "Пятёрочка",
        },
        {
          "name": "Бананы 1кг",
          "price": 45,
          "image": null,
          "store": "Перекрёсток",
        },
        {
          "name": "Куриная грудка",
          "price": 100,
          "image": null,
          "store": "Перекрёсток",
        },
        {
          "name": "Рис 1кг",
          "price": 70,
          "image": null,
          "store": "Пятёрочка",
        },
        {
          "name": "Помидоры 1кг",
          "price": 50,
          "image": null,
          "store": "Перекрёсток",
        },
        {
          "name": "Йогурт 500г",
          "price": 30,
          "image": null,
          "store": "Пятёрочка",
        },
        {
          "name": "Паста 500г",
          "price": 25,
          "image": null,
          "store": "Пятёрочка",
        },
        {
          "name": "Молоко (3%) 1л",
          "price": 60,
          "image": null,
          "store": "Перекрёсток",
        },
        {
          "name": "Морковь 1кг",
          "price": 35,
          "image": null,
          "store": "Пятёрочка",
        }
      ],
      fav:new Set(),
      cart:[],
      cartSet: new Set(),
      tab: 1 //1=main; 2=fvrt; 3;cart
    };
  }

  handleRead = async () => {
    try {
      const response = await fetch('product_list.json');
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.log('Error:', error);
    }
  };


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
    console.log("Updated fav:", this.state.fav);
  };

  handleAddToCart = (product) => {
    this.setState({
      cart: [...this.state.cart, product]
    }, () => {
      console.log('Updated cart:', this.state.cart);
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
        console.log('Updated Cart Array:', this.state.cart);
        this.changeCartSet();
      });
    }
  }
  
  changeCartSet = () => {
    const { cart } = this.state;
    const newCartSet = new Set(cart);
    this.setState({ cartSet: newCartSet }, () => {
      console.log('Updated Cart Set:', this.state.cartSet);
    });
  };

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
  
  renderContent() {
    const { tab, products, searchField } = this.state;
  
    const filteredProducts = products.filter((product) => {
      return product.name.toLowerCase().includes(searchField);
    });
    const totalPrice = () => {
      const { cart } = this.state;
      return cart.reduce((total, item) => total + item.price, 0);
    }
    return (
      <div className="App">
        <button onClick={this.handleClick}>product_list.json</button>
        <div>
          <button onClick={() => this.switchTab(1)} style={{ marginRight: '10px' }}>Все товары</button>
          <button onClick={() => this.switchTab(2)} style={{ marginRight: '10px' }}>Избранное</button>
          <button onClick={() => this.switchTab(3)} style={{ marginRight: '10px' }}>Корзина</button>
        </div>
  
        {tab === 1 && (                   //все = filteredProducts
          <div>
            <input 
              className='searchBox'
              type='search'
              placeholder='Поиск' 
              onChange={(event) => { 
                const searchField = event.target.value.toLowerCase(); 
                this.setState({ searchField }); 
              }} 
            /> 
            <hr />
            
            {filteredProducts.map((product) => ( 
              <div key={product.id}> 
                <div><h3>{product.name} <button onClick={() => this.handleToggleFav(product)}>♡</button></h3></div>
                <div>{product.store}: {product.price}₽</div> 
                <div>
                  <button onClick={() => this.handleAddToCart(product)}>+</button> 
                  {"    "+this.cartCount(product)+"   "}
                  <button onClick={() => this.handleRemoveFromCart(product)}>-</button> 
                </div>
                <hr /> 
              </div> 
            ))}
          </div>
        )}
  
        {tab === 2 && (                 //избранное = fav
          <div>
            {[...this.state.fav].map((product) => ( 
              <div key={product.id}> 
                <div><h3>{product.name}<button onClick={() => this.handleToggleFav(product)}>♡</button></h3></div>
                <div>{product.store}: {product.price}₽</div> 
                <div>
                  <button onClick={() => this.handleAddToCart(product)}>+</button> 
                  {"    "+this.cartCount(product)+"   "}
                  <button onClick={() => this.handleRemoveFromCart(product)}>-</button> 
                </div>
                <hr /> 
              </div> 
            ))}
          </div>
        )}
  
        {tab === 3 && (                 //корзина = cartSet
        <div>
          <hr />
          {[...this.state.cartSet].map((product) => (
            <div key={product.id}>
              <div><h3>{product.name}<button onClick={() => this.handleToggleFav(product)}>♡</button></h3></div>
              <div>{product.store}: {product.price}₽</div>
                <div>
                  <button 
                    onClick={() => this.handleAddToCart(product)}>
                    +</button> 
                  {"    "+this.cartCount(product)+"   "}
                  <button 
                    onClick={() => this.handleRemoveFromCart(product)}>
                    -</button> 
                </div>
              <div>{this.cartCount}</div> 
              <hr />
            </div>
          ))}
          <h2>{totalPrice()} ₽</h2>
        </div>
      )}
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
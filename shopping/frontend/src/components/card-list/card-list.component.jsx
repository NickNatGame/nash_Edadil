import {Component} from 'react';
import './card-list.styles.css'
class CardList extends Component{
    render(){
        console.log(this.props);
        const {products,onAddToCart, onRemoveFromCart, cartCount, onToggleFav}=this.props;

        return (
            <div className='card-list'>
                {products.map((product)=>(
                    <div className='card-container' key={product.id}>
                        <img alt={product.name} src={product.image} height="210" width="210" />
                        <div><h3>{product.name} <button onClick={() => onToggleFav(product)}>♡</button></h3></div>
                        <p> {product.store}: {product.price}₽</p>
                        <div>
                            <button onClick={() => onRemoveFromCart(product)}>-</button>
                            <span>  {cartCount(product)}    </span>
                            <button onClick={() => onAddToCart(product)}>+</button>
                        </div>
                            
                    </div>
                ))} 
            </div>
        );
    }
}

export default CardList
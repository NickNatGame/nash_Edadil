import {Component} from 'react';
import './card-list.styles.css'
class CardList extends Component{
    render(){
        const {products,onAddToCart, onRemoveFromCart, cartCount, onToggleFav}=this.props;

        return (
            <div className='card-list'>
                {products.map((product, i)=>(
                    <div className='card-container' key={i}>
                        <div className='image-container'>
                            <img className="card-image" alt={product.name} src={product.image} />
                        </div>
                        
                        <div><h3>{product.name} </h3></div>
                        <p> {product.store}: {product.price}₽</p>
                        <div>
                            <button className="button button_type_small" onClick={() => onRemoveFromCart(product)}>-</button>
                            <span>  {cartCount(product)}    </span>
                            <button className="button button_type_small" onClick={() => onAddToCart(product)}>+</button>
                            <button className="button button_type_small" onClick={() => onToggleFav(product)}>♡</button>
                        </div>
                            
                    </div>
                ))} 
            </div>
        );
    }
}

export default CardList
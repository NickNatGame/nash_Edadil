import {Component} from 'react';
import './card-list.styles.css'
class CardList extends Component{
    render(){
        console.log(this.props);
        const {products}=this.props;

        return (
            <div className='card-list'>
                {products.map((product)=>(
                    <div className='card-container' key={product.id}>
                        <img alt={product.name} src={product.image} height="210" width="210" />
                        <h3>{product.name}</h3>
                        <p> {product.store}: {product.price}₽</p>
                    </div>
                ))}
                <h1>war</h1>
            </div>
        );
    }
}

export default CardList
import {Component} from 'react';

class CardList extends Component{
    render(){
        console.log(this.props);
        const {products}=this.props;

        return (
            <div >
                {products.map((product)=>(
                    <h3 key={product.id}>{product.name}</h3>
                ))}
                <h1>war</h1>
            </div>
        );
    }
}

export default CardList
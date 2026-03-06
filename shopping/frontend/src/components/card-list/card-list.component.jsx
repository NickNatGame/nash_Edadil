import { Component } from 'react';
import './card-list.styles.css';

class CardList extends Component {
  getProductKey = (product) => `${product.name}-${product.store}-${product.price}`;

  render() {
    const { products, onAddToCart, onRemoveFromCart, cartCount, onToggleFav } = this.props;

    if (products.length === 0) {
      return <p className="empty-state">Ничего не найдено по вашему запросу</p>;
    }

    return (
      <div className="card-list">
        {products.map((product) => (
          <article className="card-container" key={this.getProductKey(product)}>
            <div className="image-container">
              <img className="card-image" alt={product.name} src={product.image} />
            </div>

            <h3>{product.name}</h3>
            <p className="card-meta">{product.store}: {product.price} ₽</p>
            <div className="card-controls">
              <button className="button button_type_small" onClick={() => onRemoveFromCart(product)}>-</button>
              <span>{cartCount(product)}</span>
              <button className="button button_type_small" onClick={() => onAddToCart(product)}>+</button>
              <button className="button button_type_small" onClick={() => onToggleFav(product)}>♡</button>
            </div>
          </article>
        ))}
      </div>
    );
  }
}

export default CardList;

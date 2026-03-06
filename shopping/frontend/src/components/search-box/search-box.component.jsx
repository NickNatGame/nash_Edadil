import { Component } from 'react';
import './search-box.styles.css';

class SearchBox extends Component {
  render() {
    const { className = '', placeholder = 'Поиск', onChangeHandler } = this.props;

    return (
      <input
        className={`search-box ${className}`.trim()}
        type="search"
        placeholder={placeholder}
        onChange={onChangeHandler}
      />
    );
  }
}

export default SearchBox;

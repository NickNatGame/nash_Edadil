const apiOptions = {
    baseUrl: process.env.REACT_APP_API_URL || "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
        "Accept":"*/*",
    },
};

class Api {
    constructor(options){
        this._baseUrl = options.baseUrl;
        this._headers = options.headers;
    }
    
_checkStatus(res) {
    if (res.ok) {
        return res.json();
    }
    else {
        return Promise.reject(`Ошибка ${res.status}`);
    }
}

getAllProducts() {
    return fetch(`${this._baseUrl}/products/`, {
        method: "GET",
        headers: this._headers,
        
    })
    .then(res => this._checkStatus(res));
    
}

getAnalysedCost(data) {
    return fetch(`${this._baseUrl}/analyze/`, {
        method: "POST",
        headers: this._headers,
        body: data,
    })
    .then((res) => this._checkStatus(res))
}
}

const api = new Api(apiOptions);
export default api;

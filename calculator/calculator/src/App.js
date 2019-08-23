import React, {Component} from 'react';
import './App.css';

class App extends Component() {    
    constructor() {
    	super();
    	this.state = {
    	    result: ""
    	};
    }

    onClick = button => {
    	this.setState({
    	    result: this.state.result + button
    	});
    }

    render() {
	return (
	    <div className="App">
              <table class="flex-container">
		<div class="row">
		  <button>7 </button>
		  <button onclick="display()">8</button>
		  <button onclick="display()" class="btn">9</button>
		  <button onclick="display()" class="btn">/</button>
		</div>
		<div class="row">
		  <button onclick="display()" class="btn">4</button>
		  <button onclick="display()" class="btn">5</button>
		  <button onclick="display()" class="btn">6</button>
		  <button onclick="display()" class="btn">*</button>
		</div>
		<div class="row">
		  <button class="row">1 </button>
		  <button onclick="display()" class="btn">2</button>
		  <button onclick="display()" class="btn">3</button>
		  <button onclick="display()" class="btn">+</button>
		</div>
		<div class="row">
		  <button onclick="display()" class="btn">.</button>
		  <button onclick="display()" class="btn">0</button>
		  <button onclick="display()" class="btn">=</button>
		  <button onclick="display()" class="btn">-</button>
		</div>
              </table>
	    </div>
	);
    }
}

export default App;

import React, {Component} from 'react'
import {OutputComponent} from './OutputComponent.jsx'
 
export class FormComponent extends Component {
    state = {
        text: '',
        translatedText: '',
    }
    render() {
        return(
            <div>
                <form onSubmit={this.handleSubmit}>
                    <textarea onChange={this.handleOnChange}/>
                    <button>Translate</button>
                </form>
                <OutputComponent text={this.state.translatedText}/>
            </div>
        )
    }

    handleSubmit = (e) => {
        e.preventDefault();
        this.submitText(this.state.text);

    }  


    handleOnChange = (e) => {
        this.setState({
            text: e.target.value
        })
    }

    submitText = (text) => {
        fetch(`http://localhost:5000/translate`, {
            method: 'post',
            headers: {'Content-Type':'application/json'},
            body: {
                "input": this.state.text
            }
        })
        .then(response => response.json())
        .then(data => {
            this.setState({
                translatedText: data.message,
            })
        })
    }
}

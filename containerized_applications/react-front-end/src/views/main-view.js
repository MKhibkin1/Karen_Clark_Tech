import './main-view.scss'

import {Component, useInsertionEffect} from 'react'

import USAMap from "react-usa-map";

export default class MainView extends Component{

    state ={
        activeState: null,
        loading: false,
        storms: []
    }
    
    componentDidUpdate = (prevProps, prevState) => {
        if(prevState.activeState !== this.state.activeState){
            this.setState({loading: true})
            this.loadDataByState()
            console.log("updated")
        }
    }

    handleClick = (event) => {
        this.setState({activeState: event.target.dataset.name})
    }


    loadDataByState = () => {
        fetch(`http://localhost:9999/hurricane-data?state=${this.state.activeState}&land-fall-date&name&max-wind-speed`)
        .then(resp => resp.json())
        .then(data => {
            this.setState({loading: false, storms: data.storms})
            console.log(data)
        })
    }


    renderStormInfo = () => {
        if(!this.state.activeState){
            return(
                <div className="intructions">
                    Select a state to see hurricanes that made landfall there.
                </div>
            )
        }

        if(this.state.storms.length ===0){
            return(
                <div>
                    {this.state.activeState} does not have any hurricanes that made landfall according to HURDAT.
                </div>

            )
        }

        if(this.state.loading) return

        return(
            <div className="storms-display">
                State: {this.state.activeState}
                <div className="storms">
                    {this.state.storms.map((storm, index) => {
                        return(
                            <>
                                <div className="data-tag"> Name: </div>
                                <div className="data-piece">{storm.name} </div>

                                <div className="data-tag"> Landfall Date: </div>
                                <div className="data-piece"> {new Date(storm.landFallDate).toDateString()}</div>
                                
                                <div className="data-tag"> Max Wind Speed: </div>
                                <div className="data-piece"> {storm.maxWindSpeed} </div>
                                <div className="spacer"> </div>
                            </>
                        )

                    })}
                </div>
            </div>
        )
    }

    renderLoading = () => {
        if(!this.state.loading) return
        return(
            <h5> Loading... </h5>
        )
    }

    statesCustomConfig = () => {
        if(!this.state.activeState) return
        return {
          [this.state.activeState] : {
              fill: "navy"
          }
        };
      };


    render(){
        return(
            <div className="main-view">
                <div className="header">
                    <h1>Karen Clark Interview Question</h1>
                    <h4> Huricane Report by state</h4>
                </div>


                <USAMap customize={this.statesCustomConfig()} 
                    onClick={this.handleClick}>

                </USAMap>

                <div className="data-display">
                    {this.renderLoading()}
                    {this.renderStormInfo()}
                </div>


            </div>

        )
    }

}
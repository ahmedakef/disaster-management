import React, { Component } from 'react';
import './App.css';
import {Map, InfoWindow, Marker, GoogleApiWrapper , polygon , circle} from 'google-maps-react';
import { render } from 'react-dom';
import home from './home2.png';
import Modal from 'react-modal';
import SlidingPane from 'react-sliding-pane';
import 'react-sliding-pane/dist/react-sliding-pane.css';
import Request from 'react-http-request';
import {BrowserRouter as Router , Link} from 'react-router-dom'
import Route from 'react-router-dom/Route'

class App extends Component {

      handleSubmit(data) {
          console.log('form submission data', data);
      }
      constructor(props) {
        super(props);
        this.state = {
            isPaneOpen: false,
            isPaneOpenLeft: false
        };
    }

    componentDidMount() {
        Modal.setAppElement(this.el);
    }

  render() {


    const position = { lat: 31.197839, lng: 31.921121 };
    const icon = { url: 'https://scontent-mrs1-1.xx.fbcdn.net/v/t1.15752-0/p280x280/42654138_267876777233424_7028610389587787776_n.png?_nc_cat=111&oh=e4f5912bb225217d4cd3e958b50b14e0&oe=5C25CD1D', scaledSize: { width: 20, height: 20  } };
    <Request
            url='https://akef-test-ibm.eu-gb.mybluemix.net/disasters/'
            method='get'
            accept='application/json'
            verbose={true}
          >
                {
                    ({error, result, loading}) => {
                      if (loading) {
                        return <div>loading...</div>;
                      } else {
                        return <div>{ JSON.stringify(result.body) }</div>;
                      }
                    }
                  }
      </Request>

    return (
      <Router>
        <div className="App">



          <Route path="/" exact render={
              () =>{
                return(
                  <div>
                      <div ref={ref => this.el = ref}>

                        <header className="App-header">
                          <div className="homebtn">
                            <button className="hbtn" onClick={ () => this.setState({ isPaneOpenLeft: true }) }>
                              <img src={home} alt="home icon"/>
                            </button>
                          </div>
                          <h1 className="App-title">Welcome to Desaster Managemet</h1>
                        </header>



                        <SlidingPane className="slidepane"
                            isOpen={ this.state.isPaneOpenLeft }
                            from='left'
                            width='200px'
                            onRequestClose={ () => this.setState({ isPaneOpenLeft: false }) }>

                            <Link to="/Login" className="atag">Log in</Link>
                            <Link to="/Register" className="atag">Register</Link>
                            <Link to="/" className="atag">Home</Link>
                            <Link to="/Urgent" className="atag">Urgent</Link>

                        </SlidingPane>
                      </div>
                      <div className="rightbar">
                    <Map google={this.props.google}
                      zoom={6}
                      initialCenter={{ lat: 27.130638, lng: 30.431850 }}>

                      <Marker position={{ lat: 24.334667, lng: 35.034377 }} icon={icon} />
                      <Marker position={{ lat: 31.162664, lng: 30.815792 }} icon={icon} />

                      <Marker position={position} icon={icon} />

                    </Map>
                   </div>
                 </div>
                );
              }
            }/>


          <Route path="/Urgent" exact render={
                () =>{
                  return(
                    <div>
                        <div ref={ref => this.el = ref}>

                          <header className="App-header">
                            <div className="homebtn">
                              <button className="hbtn" onClick={ () => this.setState({ isPaneOpenLeft: true }) }>
                                <img src={home} alt="home icon"/>
                              </button>
                            </div>
                            <h1 className="App-title">Welcome to Desaster Managemet</h1>
                          </header>



                          <SlidingPane className="slidepane"
                              isOpen={ this.state.isPaneOpenLeft }
                              from='left'
                              width='200px'
                              onRequestClose={ () => this.setState({ isPaneOpenLeft: false }) }>

                              <Link to="/" className="atag">Home</Link>
                              <Link to="/Urgent" className="atag">Urgent</Link>

                          </SlidingPane>
                        </div>
                        <div className="rightbar">
                      <Map google={this.props.google}
                        zoom={6}
                        initialCenter={{ lat: 27.130638, lng: 30.431850 }}>

                        <Marker position={{ lat: 24.334667, lng: 35.034377 }}  />
                        <Marker position={{ lat: 31.162664, lng: 30.815792 }}  />
                        <Marker position={position}  />

                      </Map>
                     </div>
                   </div>
                  );
                }
              }/>


          <Route path="/Register" exact render={
                      () =>{
                        return(
                          <div>
                              <div ref={ref => this.el = ref}>

                                <header className="App-header">
                                  <div className="homebtn">
                                    <button className="hbtn" onClick={ () => this.setState({ isPaneOpenLeft: true }) }>
                                      <img src={home} alt="home icon"/>
                                    </button>
                                  </div>
                                  <h1 className="App-title">Welcome to Desaster Managemet</h1>
                                </header>



                                <SlidingPane className="slidepane"
                                    isOpen={ this.state.isPaneOpenLeft }
                                    from='left'
                                    width='200px'
                                    onRequestClose={ () => this.setState({ isPaneOpenLeft: false }) }>

                                          <Link to="/" className="atag">Home</Link>
                                          <Link to="/Urgent" className="atag">Urgent</Link>

                                </SlidingPane>
                              </div>

                              <form name="form" onSubmit={this.handleSubmit}>

                                <div className="top-row">
                                  <div className="field-wrap">
                                    <label>
                                      First Name<span className="req">*</span>
                                    </label>
                                    <input type="text" required autocomplete="off" />
                                  </div>

                                  <div className="field-wrap">
                                    <label>
                                      Phone Number<span className="req">*</span>
                                    </label>
                                    <input type="text"required autocomplete="off"/>
                                  </div>
                                </div>


                                  <div className="field-wrap">
                                    <label>
                                      Email Address<span className="req">*</span>
                                    </label>
                                    <input type="email"required autocomplete="off"/>
                                  </div>

                                  <div className="field-wrap">
                                    <label>
                                       Password<span className="req">*</span>
                                    </label>
                                    <input type="password"required autocomplete="off"/>
                                  </div>

                                      <button type="submit" className="button button-block">
                                        <Link to="/Home" className="sub">Register</Link></button>

                              </form>
                         </div>
                        );
                      }
                    }/>

          <Route path="/Login" exact render={
                                () =>{
                                  return(
                                    <div>
                                        <div ref={ref => this.el = ref}>

                                          <header className="App-header">
                                            <div className="homebtn">
                                              <button className="hbtn" onClick={ () => this.setState({ isPaneOpenLeft: true }) }>
                                                <img src={home} alt="home icon"/>
                                              </button>
                                            </div>
                                            <h1 className="App-title">Welcome to Desaster Managemet</h1>
                                          </header>



                                          <SlidingPane className="slidepane"
                                              isOpen={ this.state.isPaneOpenLeft }
                                              from='left'
                                              width='200px'
                                              onRequestClose={ () => this.setState({ isPaneOpenLeft: false }) }>

                                                    <Link to="/" className="atag">Home</Link>
                                                    <Link to="/Urgent" className="atag">Urgent</Link>

                                          </SlidingPane>
                                        </div>

                                        <form name="form" onSubmit={this.handleSubmit}>


                                            <div className="field-wrap">
                                              <label>
                                                Email Address<span className="req">*</span>
                                              </label>
                                              <input type="email"required autocomplete="off"/>
                                            </div>

                                            <div className="field-wrap">
                                              <label>
                                                 Password<span className="req">*</span>
                                              </label>
                                              <input type="password"required autocomplete="off"/>
                                            </div>

                                            <button type="submit" className="button button-block">
                                                  <Link to="/Home" className="sub">Log in</Link></button>

                                        </form>
                                   </div>
                                  );
                                }
                              }/>

         <Route path="/Home" exact render={
                                        () =>{
                                          return(
                                            <div>
                                                <div ref={ref => this.el = ref}>

                                                  <header className="App-header">
                                                    <div className="homebtn">
                                                      <button className="hbtn" onClick={ () => this.setState({ isPaneOpenLeft: true }) }>
                                                        <img src={home} alt="home icon"/>
                                                      </button>
                                                    </div>
                                                    <h1 className="App-title">Welcome to Desaster Managemet</h1>
                                                  </header>



                                                  <SlidingPane className="slidepane"
                                                      isOpen={ this.state.isPaneOpenLeft }
                                                      from='left'
                                                      width='200px'
                                                      onRequestClose={ () => this.setState({ isPaneOpenLeft: false }) }>

                                                      <Link to="/" className="atag">Home</Link>
                                                      <Link to="/Urgent" className="atag">Urgent</Link>

                                                  </SlidingPane>
                                                </div>
                                                <div className="rightbar">
                                              <Map google={this.props.google}
                                                zoom={6}
                                                initialCenter={{ lat: 27.130638, lng: 30.431850 }}>

                                                <Marker position={{ lat: 24.334667, lng: 35.034377 }} icon={icon} />
                                                <Marker position={{ lat: 31.162664, lng: 30.815792 }} icon={icon} />

                                                <Marker position={position} icon={icon} />

                                              </Map>
                                             </div>
                                           </div>
                                          );
                                        }
                                      }/>


        </div>
      </Router>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: ("AIzaSyCHWCNN2BbQ4d1rBQgrwccVwMbt1Sq-AIM")
})(App)

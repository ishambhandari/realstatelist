
import React from 'react'
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import Home from './containers/Home'
import About from './containers/About'
import Contact from './containers/Contact'
import ListingDetail from './containers/ListingDetail'
import SignUp from './containers/SignUp'
import SignIn from './containers/SignIn'
import Listings from './containers/Listings'
import NotFound from './components/NotFound'
import Layout from './higherorder/Layout'

import {Provider} from 'react-redux'
import store from './store'

import './sass/main.scss'

function App() {
  return (
    <div className="App">
      <Provider store = {store}>
        <Router>
          <Layout>
            {/* Makes sure switch only displays 1 component at a time */}
            <Switch> 
              <Route exact path = '/' component = {Home} />
              <Route exact path = '/about' component = {About} />
              <Route exact path = '/contact' component = {Contact} />
              <Route exact path = '/listings' component = {Listings} />
              <Route exact path = '/listings/:id' component = {ListingDetail} />
              <Route exact path = '/signin' component = {SignIn} />
              <Route exact path = '/signout' component = {SignUp}/>
              <Route component={NotFound}/>
            </Switch>
          </Layout>
        </Router>
      </Provider>
    </div>
  );
}

export default App;

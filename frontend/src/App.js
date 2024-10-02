// // src/App.js
// import './App.css';
// import React, { useEffect } from 'react';
// import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
// import { useDispatch } from 'react-redux';
// import Login from './components/Login';
// import Profile from './components/Profile';
// import Home from './components/Home';
// import PrivateRoute from './utils/PrivateRoute';
// import authService from './utils/authService';
// import { loginSuccess } from './store/authSlice';

// const App = () => {
//   const dispatch = useDispatch();

//   useEffect(() => {
//     // Check if user is authenticated on app load
//     if (authService.isAuthenticated()) {
//       const userData = {
//         access: localStorage.getItem('accessToken'),
//         refresh: localStorage.getItem('refreshToken')
//       };
//       dispatch(loginSuccess(userData));
//     }
//   }, [dispatch]);

//   return (
//     <Router>
//       <nav>
//         <ul>
//           <li><Link to="/">Home</Link></li>
//           <li><Link to="/login">Login</Link></li>
//           <li><Link to="/profile">Profile</Link></li>
//         </ul>
//       </nav>
//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/login" element={<Login />} />
//         <Route
//           path="/profile"
//           element={
//             <PrivateRoute>
//               <Profile />
//             </PrivateRoute>
//           }
//         />
//       </Routes>
//     </Router>
//   );
// };

// export default App;

// src/App.js
import './App.css';
import React, { useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import Login from './components/Login';
import Profile from './components/Profile';
import Home from './components/Home';
import PrivateRoute from './utils/PrivateRoute';
import authService from './utils/authService';
import { loginSuccess } from './store/authSlice';

const App = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    // Check if user is authenticated on app load
    if (authService.isAuthenticated()) {
      const userData = {
        access: localStorage.getItem('accessToken'),
        refresh: localStorage.getItem('refreshToken')
      };
      dispatch(loginSuccess(userData));
    }
  }, [dispatch]);

  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/login">Login</Link></li>
          <li><Link to="/profile">Profile</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/profile"
          element={
            <PrivateRoute>
              <Profile />
            </PrivateRoute>
          }
        />
      </Routes>
    </Router>
  );
};

export default App;
// Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Navbar.module.css';

const Navbar = () => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>Recent Goals</div>
      <div className={styles.links}>
        <Link to="/news" className={styles.link}>News</Link>
        <Link to="/recent-goals" className={styles.link}>Recent Goals</Link>
        <Link to="/matches" className={styles.link}>Matches</Link>
        <Link to="/games-results" className={styles.link}>Live Games</Link>
      </div>
    </nav>
  );
};

export default Navbar;

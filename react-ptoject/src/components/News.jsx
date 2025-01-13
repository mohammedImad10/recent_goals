// News.js
import React from 'react';
import styles from './News.module.css';

const News = () => {
  const articles = [
    { title: "Team A's Stunning Comeback", summary: "Team A rallied from 2 goals down to win." },
    { title: "Player X Breaks Record", summary: "Player X scored the fastest goal in history." },
  ];

  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>Latest Football News</h1>
      <div className={styles.articles}>
        {articles.map((article, index) => (
          <div key={index} className={styles.card}>
            <h2 className={styles.title}>{article.title}</h2>
            <p className={styles.summary}>{article.summary}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default News;

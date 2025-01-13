// Matches.js
import React from 'react';
import styles from './Matches.module.css';

const Matches = () => {
  const matches = [
    { teamA: "Team A", teamB: "Team B", time: "18:00", result: "2-1" },
    { teamA: "Team C", teamB: "Team D", time: "20:00", result: "1-1" },
  ];

  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>Upcoming Matches</h1>
      <ul className={styles.matchList}>
        {matches.map((match, index) => (
          <li key={index} className={styles.matchCard}>
            <div className={styles.teams}>
              <span className={styles.team}>{match.teamA}</span> vs <span className={styles.team}>{match.teamB}</span>
            </div>
            <div className={styles.details}>
              <span>{match.time}</span> | Result: {match.result}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Matches;

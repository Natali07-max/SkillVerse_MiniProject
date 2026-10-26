import React from "react";
import {
  Trophy,
  Medal,
  Crown,
  Zap,
  Flame,
  Target,
  Star,
} from "lucide-react";
import "../styles/leaderboard.css";

const players = [
  { name: "Aarav", xp: 9850, level: 18, streak: 12, games: 42, avatar: "A" },
  { name: "Priya", xp: 9200, level: 17, streak: 9, games: 38, avatar: "P" },
  { name: "Rahul", xp: 8750, level: 16, streak: 7, games: 35, avatar: "R" },
  { name: "Ananya", xp: 8100, level: 15, streak: 6, games: 31, avatar: "A" },
  { name: "Dhara", xp: 7600, level: 14, streak: 10, games: 29, avatar: "D" },
  { name: "Ishaan", xp: 7200, level: 13, streak: 4, games: 26, avatar: "I" },
  { name: "Sneha", xp: 6850, level: 12, streak: 8, games: 24, avatar: "S" },
  { name: "Kabir", xp: 6300, level: 11, streak: 5, games: 21, avatar: "K" },
];

const rankIcons = {
  1: <Crown size={19} />,
  2: <Medal size={19} />,
  3: <Trophy size={19} />,
};

function Leaderboard() {
  const sortedPlayers = [...players].sort((a, b) => b.xp - a.xp);
  const topThree = sortedPlayers.slice(0, 3);
  const currentUser = JSON.parse(
    localStorage.getItem("currentUser") || "null"
  );
  const username = currentUser?.username || "Guest Player";
  const myRank = sortedPlayers.findIndex(
    (player) =>
      player.name.toLowerCase() === username.toLowerCase()
  );

  return (
    <div className="leaderboard-page">
      <div className="leaderboard-header">
        <div>
          <span className="lb-eyebrow">
            <Trophy size={16} /> COMPETE • LEARN • WIN
          </span>
          <h1>
            Hall of <span>Legends</span>
          </h1>
          <p>Every challenge takes you one step closer to greatness.</p>
        </div>

        <div className="lb-season">
          <Star size={18} />
          <div>
            <strong>Season 01</strong>
            <small>Learning Champions</small>
          </div>
        </div>
      </div>

      <div className="lb-stats">
        <div className="lb-stat-card">
          <div className="lb-stat-icon purple">
            <Trophy size={21} />
          </div>
          <div>
            <small>Total Players</small>
            <h2>128</h2>
          </div>
        </div>

        <div className="lb-stat-card">
          <div className="lb-stat-icon yellow">
            <Zap size={21} />
          </div>
          <div>
            <small>XP Available</small>
            <h2>1.2M</h2>
          </div>
        </div>

        <div className="lb-stat-card">
          <div className="lb-stat-icon orange">
            <Flame size={21} />
          </div>
          <div>
            <small>Daily Challenge</small>
            <h2>Active</h2>
          </div>
        </div>

        <div className="lb-stat-card">
          <div className="lb-stat-icon blue">
            <Target size={21} />
          </div>
          <div>
            <small>Your Position</small>
            <h2>{myRank >= 0 ? `#${myRank + 1}` : "Unranked"}</h2>
          </div>
        </div>
      </div>

      <section className="lb-podium-section">
        <div className="lb-section-heading">
          <div>
            <h2>Top Champions</h2>
            <p>The brightest minds of this season.</p>
          </div>
          <span className="lb-live">
            <span /> LIVE RANKINGS
          </span>
        </div>

        <div className="lb-podium">
          {[topThree[1], topThree[0], topThree[2]].map(
            (player, index) => {
              const rank = sortedPlayers.indexOf(player) + 1;

              return (
                <div
                  className={`lb-champion rank-${rank}`}
                  key={player.name}
                >
                  <div className="lb-crown">
                    {rankIcons[rank]}
                  </div>

                  <div className="lb-champion-avatar">
                    {player.avatar}
                  </div>

                  <span className="lb-rank-label">
                    {rank === 1
                      ? "CHAMPION"
                      : rank === 2
                      ? "RUNNER UP"
                      : "THIRD PLACE"}
                  </span>

                  <h3>{player.name}</h3>
                  <p>Level {player.level} Explorer</p>

                  <div className="lb-champion-xp">
                    <Zap size={16} />
                    {player.xp.toLocaleString()} XP
                  </div>

                  <div className="lb-podium-base">
                    <span>{rank}</span>
                  </div>
                </div>
              );
            }
          )}
        </div>
      </section>

      <section className="lb-table-section">
        <div className="lb-section-heading">
          <div>
            <h2>Player Rankings</h2>
            <p>Keep learning to climb the leaderboard.</p>
          </div>
          <span className="lb-sorted">Sorted by XP ↓</span>
        </div>

        <div className="lb-table-wrapper">
          <table className="lb-table">
            <thead>
              <tr>
                <th>RANK</th>
                <th>PLAYER</th>
                <th>LEVEL</th>
                <th>GAMES</th>
                <th>STREAK</th>
                <th>TOTAL XP</th>
              </tr>
            </thead>

            <tbody>
              {sortedPlayers.map((player, index) => {
                const isCurrentUser =
                  player.name.toLowerCase() ===
                  username.toLowerCase();

                return (
                  <tr
                    key={player.name}
                    className={isCurrentUser ? "lb-current-user" : ""}
                  >
                    <td>
                      <span className={`lb-rank rank-number-${index + 1}`}>
                        {index + 1 <= 3
                          ? rankIcons[index + 1]
                          : `#${index + 1}`}
                      </span>
                    </td>

                    <td>
                      <div className="lb-player-info">
                        <div className="lb-table-avatar">
                          {player.avatar}
                        </div>
                        <div>
                          <strong>
                            {player.name}
                            {isCurrentUser && (
                              <span className="lb-you">YOU</span>
                            )}
                          </strong>
                          <small>Quest Explorer</small>
                        </div>
                      </div>
                    </td>

                    <td>
                      <span className="lb-level">
                        Lv. {player.level}
                      </span>
                    </td>

                    <td>{player.games}</td>

                    <td>
                      <span className="lb-streak">
                        <Flame size={15} /> {player.streak} days
                      </span>
                    </td>

                    <td>
                      <strong className="lb-xp">
                        {player.xp.toLocaleString()}
                      </strong>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>

        <div className="lb-footer-note">
          <Trophy size={17} />
          <span>Complete more quests, earn XP, and become a legend!</span>
        </div>
      </section>
    </div>
  );
}

export default Leaderboard;
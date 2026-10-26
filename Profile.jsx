import Sidebar from "../components/Sidebar";
import {
  User,
  Trophy,
  Flame,
  Zap,
  Brain,
  Target,
  Puzzle,
  Award,
  Calendar,
  Edit3
} from "lucide-react";

const Profile = () => {
  const achievements = [
    {
      title: "Memory Master",
      icon: <Brain size={24} />,
      description: "Scored 90% in Memory Game"
    },
    {
      title: "7 Day Warrior",
      icon: <Flame size={24} />,
      description: "Maintained a 7-day streak"
    },
    {
      title: "Speed Demon",
      icon: <Zap size={24} />,
      description: "Completed a game in under 60 seconds"
    },
    {
      title: "Perfect Score",
      icon: <Trophy size={24} />,
      description: "Achieved 100% accuracy"
    }
  ];

  const skills = [
    { name: "Memory", value: 85, icon: <Brain size={18} /> },
    { name: "Focus", value: 72, icon: <Target size={18} /> },
    { name: "Logic", value: 68, icon: <Puzzle size={18} /> },
    { name: "Problem Solving", value: 78, icon: <Award size={18} /> }
  ];

  const activities = [
    {
      title: "Completed Memory Master",
      time: "Today, 10:30 AM",
      xp: "+500 XP"
    },
    {
      title: "Completed Focus Sprint",
      time: "Yesterday, 6:45 PM",
      xp: "+350 XP"
    },
    {
      title: "Unlocked Logic Quest",
      time: "2 days ago",
      xp: "+200 XP"
    }
  ];

  return (
    <div className="app-layout">
      <Sidebar />

      <main className="main-content">

        {/* PROFILE HEADER */}
        <div className="profile-hero glass-card">

          <div className="profile-cover"></div>

          <div className="profile-main">

            <div className="profile-avatar">
              D
              <div className="online-dot"></div>
            </div>

            <div className="profile-user-info">
              <p className="section-label">SKILLQUEST PLAYER</p>

              <h1>Dhara Dhotre</h1>

              <p className="profile-email">
                dhara@example.com
              </p>

              <div className="profile-tags">
                <span>🎮 Explorer</span>
                <span>⚡ Level 12</span>
                <span>🔥 14 Day Streak</span>
              </div>
            </div>

            <button className="edit-profile-btn">
              <Edit3 size={17} />
              Edit Profile
            </button>

          </div>
        </div>

        {/* STATS */}
        <div className="profile-stats-grid">

          <div className="profile-stat glass-card">
            <div className="profile-stat-icon xp-icon">
              <Zap size={24} />
            </div>

            <div>
              <p>Total XP</p>
              <h2>12,450</h2>
              <span>+850 this week</span>
            </div>
          </div>

          <div className="profile-stat glass-card">
            <div className="profile-stat-icon level-icon">
              <Trophy size={24} />
            </div>

            <div>
              <p>Current Level</p>
              <h2>12</h2>
              <span>750 XP to Level 13</span>
            </div>
          </div>

          <div className="profile-stat glass-card">
            <div className="profile-stat-icon streak-icon">
              <Flame size={24} />
            </div>

            <div>
              <p>Longest Streak</p>
              <h2>14 Days</h2>
              <span>Keep the fire alive!</span>
            </div>
          </div>

          <div className="profile-stat glass-card">
            <div className="profile-stat-icon game-icon-profile">
              <User size={24} />
            </div>

            <div>
              <p>Games Played</p>
              <h2>28</h2>
              <span>4 games this week</span>
            </div>
          </div>

        </div>

        <div className="profile-content-grid">

          {/* SKILLS */}
          <div className="profile-section glass-card">

            <div className="profile-section-heading">
              <div>
                <p className="section-label">PERFORMANCE</p>
                <h2>My Skills</h2>
              </div>

              <Brain size={28} />
            </div>

            <div className="skills-list">

              {skills.map((skill, index) => (
                <div className="skill-item" key={index}>

                  <div className="skill-header">
                    <div className="skill-name">
                      {skill.icon}
                      <span>{skill.name}</span>
                    </div>

                    <strong>{skill.value}%</strong>
                  </div>

                  <div className="skill-progress-track">
                    <div
                      className="skill-progress-fill"
                      style={{ width: `${skill.value}%` }}
                    ></div>
                  </div>

                </div>
              ))}

            </div>

          </div>

          {/* LEVEL PROGRESS */}
          <div className="level-card glass-card">

            <p className="section-label">PLAYER PROGRESS</p>

            <div className="level-number">
              12
            </div>

            <h2>Explorer</h2>

            <p>
              Keep completing quests to reach the next level!
            </p>

            <div className="level-progress-info">
              <span>12,450 XP</span>
              <span>13,200 XP</span>
            </div>

            <div className="level-progress-track">
              <div className="level-progress-fill"></div>
            </div>

            <p className="xp-needed">
              Only 750 XP until Level 13 🚀
            </p>

          </div>

        </div>

        {/* ACHIEVEMENTS */}
        <div className="achievements-section">

          <div className="section-top">
            <div>
              <p className="section-label">YOUR COLLECTION</p>
              <h2>Achievements & Badges</h2>
            </div>

            <span className="achievement-count">
              16 Unlocked
            </span>
          </div>

          <div className="achievement-grid">

            {achievements.map((achievement, index) => (
              <div
                className="achievement-card glass-card"
                key={index}
              >

                <div className="achievement-icon">
                  {achievement.icon}
                </div>

                <div>
                  <h3>{achievement.title}</h3>
                  <p>{achievement.description}</p>
                </div>

              </div>
            ))}

          </div>

        </div>

        {/* RECENT ACTIVITY */}
        <div className="activity-section glass-card">

          <div className="profile-section-heading">

            <div>
              <p className="section-label">LEARNING JOURNEY</p>
              <h2>Recent Activity</h2>
            </div>

            <Calendar size={25} />

          </div>

          <div className="activity-list">

            {activities.map((activity, index) => (
              <div className="activity-item" key={index}>

                <div className="activity-number">
                  {index + 1}
                </div>

                <div className="activity-info">
                  <h3>{activity.title}</h3>
                  <p>{activity.time}</p>
                </div>

                <span className="activity-xp">
                  {activity.xp}
                </span>

              </div>
            ))}

          </div>

        </div>

      </main>
    </div>
  );
};

export default Profile;
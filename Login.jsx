import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Mail, Lock, Sparkles, Eye, EyeOff } from "lucide-react";
import axios from "axios";

const Login = () => {
  const navigate = useNavigate();

  const [showPassword, setShowPassword] = useState(false);

  const [formData, setFormData] = useState({
    
    email: "",
    password: ""
  });

  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setError("");
    setMessage("");

    if (!formData.email || !formData.password) {
      setError("Please fill in all fields.");
      return;
    }

    try {
      /*
      BACKEND CONNECTION

      const response = await axios.post(
        "http://localhost:5000/api/login",
        formData
      );

      localStorage.setItem("token", response.data.token);
      */

      localStorage.setItem("token", "demo-token");

      setMessage("Login successful! Welcome back, Player!");

      setTimeout(() => {
        navigate("/dashboard");
      }, 1000);

    } catch (err) {
      setError("Invalid email or password.");
    }
  };

  return (
    <div className="auth-page">

      <div className="auth-left">

        <div className="auth-logo">
          <Sparkles />
          <h2>SkillQuest AI</h2>
        </div>

        <div className="auth-content">

          <p className="small-title">WELCOME BACK, PLAYER</p>

          <h1>
            Continue Your
            <span> Learning Quest</span>
          </h1>

          <p className="auth-description">
            Your personalized AI-powered journey is waiting.
            Complete quests, earn XP and unlock your potential.
          </p>

          <div className="login-card glass-card">

            {error && (
              <div className="error-message">
                {error}
              </div>
            )}

            {message && (
              <div className="success-message">
                {message}
              </div>
            )}

          

            <form onSubmit={handleSubmit}>

            <label>Email Address</label>

              <div className="input-box">
                <Mail size={19} />

                <input
                  type="email"
                  name="email"
                  placeholder="Enter your email"
                  onChange={handleChange}
                />
              </div>

              <label>Password</label>

              <div className="input-box">
                <Lock size={19} />

                <input
                  type={showPassword ? "text" : "password"}
                  name="password"
                  placeholder="Enter your password"
                  onChange={handleChange}
                />

                <button
                  type="button"
                  className="eye-btn"
                  onClick={() =>
                    setShowPassword(!showPassword)
                  }
                >
                  {showPassword ? <EyeOff /> : <Eye />}
                </button>

              </div>

              <button
                type="submit"
                className="primary-btn login-btn"
              >
                Start My Quest →
              </button>

            </form>

            <p className="auth-footer">
              New to SkillQuest?
              <Link to="/signup"> Create Account</Link>
            </p>

          </div>
        </div>

      </div>

      <div className="auth-right">

        <div className="floating-orb orb1"></div>
        <div className="floating-orb orb2"></div>

        <div className="hero-quest-card glass-card">

          <p>⚡ TODAY'S QUEST</p>

          <h2>Level Up Your Mind</h2>

          <div className="xp-progress">
            <div className="xp-fill"></div>
          </div>

          <span>750 / 1000 XP</span>

          <div className="quest-icons">
            🧠 🎯 🏆 🚀
          </div>

        </div>

      </div>

    </div>
  );
};

export default Login;
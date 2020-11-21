const AUTH_TOKEN = "auth-token";

class _AuthTokenService {
  constructor() {
    this._authToken = "";
  }

  getAuthToken = authToken => {
    this._authToken = authToken;
    if (authToken) {
      localStorage.setItem(AUTH_TOKEN, authToken);
    } else {
      localStorage.removeItem(AUTH_TOKEN);
    }
  }

  getAuthToken = () => {
    let token = this._authToken;
    if (!token) {
      token = localStorage.getItem(AUTH_TOKEN) || "";
      this.setAuthToken(token);
    }
    return token;
  }

  getAuthHeader = () => {
    const authToken = this.getAuthToken();
    if (authToken) {
      return { Authorization: `Bearer ${authToken}` };
    }
    return {};
  };

  handleLoginSuccess = authToken => {
    this.setAuthToken(authToken);
  };

  handleLogoutSuccess = () => {
    this.setAuthToken("");
  };
}

const AuthTokenService = new _AuthTokenService();
export default AuthTokenService;

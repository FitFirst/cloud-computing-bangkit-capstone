const config = require("./config/config");
const Hapi = require("@hapi/hapi");
const registerAuthRoutes = require("./routes/authRoute");
const registerUserRoutes = require("./routes/userRoute");
const registerTrackerRoutes = require("./routes/trackerRoute");
const admin = require("firebase-admin");
require("./config/firebaseConfig");

(async () => {
  const server = Hapi.server({
    port: config.port,
    host: config.host,
    routes: {
      cors: {
        origin: ["*"],
      },
    },
  });

  registerAuthRoutes(server);
  registerUserRoutes(server);
  registerTrackerRoutes(server);

  try {
    await server.start();

    console.log(`Server started at: ${server.info.uri}`);
  } catch (error) {
    console.error("Server startup error:", error);
    process.exit(1);
  }
})();

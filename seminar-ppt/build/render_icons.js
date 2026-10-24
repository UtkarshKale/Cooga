// Render react-icons glyphs to PNG files for the decks.
// Usage: node render_icons.js <node_modules dir> <out dir>
const path = require("path");
const [modDir, outDir] = process.argv.slice(2);
const req = (m) => require(path.join(modDir, m));
const React = req("react");
const { renderToStaticMarkup } = req("react-dom/server");
const sharp = req("sharp");
const libs = { fa: req("react-icons/fa"), gi: req("react-icons/gi"), md: req("react-icons/md") };

const ICONS = {
  brain: ["fa", "FaBrain"], plan: ["fa", "FaProjectDiagram"], tools: ["fa", "FaTools"],
  db: ["fa", "FaDatabase"], users: ["fa", "FaUsers"], shield: ["fa", "FaShieldAlt"],
  code: ["fa", "FaCode"], search: ["fa", "FaSearch"], bug: ["fa", "FaBug"],
  robot: ["fa", "FaRobot"], cogs: ["fa", "FaCogs"], user: ["fa", "FaUserTie"],
  book: ["fa", "FaBookOpen"], plug: ["fa", "FaPlug"], check: ["fa", "FaCheckCircle"],
  warn: ["fa", "FaExclamationTriangle"], star: ["fa", "FaStar"], globe: ["fa", "FaGlobe"],
  file: ["fa", "FaFileAlt"], flag: ["fa", "FaFlagCheckered"], sync: ["fa", "FaSyncAlt"],
  chart: ["fa", "FaChartLine"], layers: ["fa", "FaLayerGroup"], satellite: ["fa", "FaSatellite"],
  tower: ["fa", "FaBroadcastTower"], comment: ["fa", "FaCommentDots"], water: ["fa", "FaWater"],
  fire: ["fa", "FaFire"], house: ["fa", "FaHouseDamage"], wind: ["fa", "FaWind"],
  route: ["fa", "FaRoute"], truck: ["fa", "FaTruck"], bell: ["fa", "FaBell"],
  map: ["fa", "FaMapMarkedAlt"], drone: ["gi", "GiDeliveryDrone"], hands: ["fa", "FaHandsHelping"],
  lightbulb: ["fa", "FaLightbulb"], eye: ["fa", "FaEye"], clock: ["fa", "FaClock"],
  balance: ["fa", "FaBalanceScale"], sitemap: ["fa", "FaSitemap"], network: ["fa", "FaNetworkWired"],
  terminal: ["fa", "FaTerminal"], quake: ["gi", "GiEarthCrack"], cyclone: ["gi", "GiTornado"],
  sensor: ["md", "MdSensors"], target: ["fa", "FaBullseye"], money: ["fa", "FaCoins"],
};
const COLORS = { w: "#FFFFFF", n: "#1F497D", b: "#4F81BD", o: "#E46C0A", r: "#C0504D", g: "#76923C" };

(async () => {
  for (const [key, [lib, name]] of Object.entries(ICONS)) {
    const Comp = libs[lib][name];
    if (!Comp) throw new Error(`missing icon ${lib}.${name}`);
    for (const [ck, col] of Object.entries(COLORS)) {
      const svg = renderToStaticMarkup(React.createElement(Comp, { color: col, size: 256 }));
      await sharp(Buffer.from(svg)).resize(256, 256).png().toFile(path.join(outDir, `${key}_${ck}.png`));
    }
  }
  console.log("ok", Object.keys(ICONS).length);
})();

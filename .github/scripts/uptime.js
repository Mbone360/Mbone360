const fs = require("fs");

const START_DATE = new Date("2005-05-08");
const NOW = new Date();

let years = NOW.getFullYear() - START_DATE.getFullYear();
let months = NOW.getMonth() - START_DATE.getMonth();
let days = NOW.getDate() - START_DATE.getDate();

if (days < 0) {
  months--;
  const prevMonth = new Date(NOW.getFullYear(), NOW.getMonth(), 0);
  days += prevMonth.getDate();
}

if (months < 0) {
  years--;
  months += 12;
}

const uptime = `${years}y ${months}m ${days}d`;

let readme = fs.readFileSync("README.md", "utf-8");

readme = readme.replace(
  /Uptime:\s+.*/g,
  `Uptime:    ${uptime}`
);

fs.writeFileSync("README.md", readme);

console.log("Updated uptime:", uptime);

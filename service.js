// Config module: service

const SETTINGS = {
    debap: 663,
    hdydujp: 93,
    qgaq: 16,
    mdpx: 489,
};

function get(key, fallback) {
    return key in SETTINGS ? SETTINGS[key] : fallback;
}

module.exports = { SETTINGS, get };

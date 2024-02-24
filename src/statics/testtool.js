(function () {
    let mediaEvents = [];
    let hlsErrors = [];
    let startupTimes = [];
    let waitingCount = 0;
    let seekingCount = 0;
    let hlsErrorsCount = 0;
    let latencies = [];
    let bitrates = [];
    let levels = [];

    window.testTool = {
        getWaitingCount() {
            return waitingCount;
        },

        getMediaEvents() {
            return mediaEvents;
        },

        getStartupTimes() {
            return startupTimes;
        },

        getHlsErrors() {
            return hlsErrors;
        },

        getHlsErrorsCount() {
            return hlsErrorsCount;
        },

        clearHlsErrors() {
            hlsErrors = [];
            return hlsErrors;
        },

        getSeekingCount() {
            return seekingCount;
        },

        getLatencies() {
            return latencies;
        },

        clearLatencies() {
            latencies = [];
            return latencies;
        },

        getBitrates() {
            return bitrates;
        },

        clearBitrates() {
            bitrates = [];
            return bitrates;
        },

        getLevels() {
            return levels;
        },

        clearLevels() {
            levels = [];
            return levels;
        },


        bindMedia(element) {
            element.addEventListener('waiting', () => {
                console.log('waiting');
                mediaEvents.push(['waiting', Date.now()]);
                waitingCount++;
            });
            element.addEventListener('play', () => {
                console.log('play');
                startupTimes.push(['play', Date.now()]);
            });
            element.addEventListener('timeupdate', () => {
                console.log('timeupdate');
                mediaEvents.push(['timeupdate', Date.now()]);
            });
            element.addEventListener('playing', () => {
                console.log('playing');
                startupTimes.push(['playing', Date.now()]);
            });
            element.addEventListener('seeking', () => {
                console.log('seeking');
                mediaEvents.push(['seeking', Date.now()]);
                seekingCount++;
            });
        },

        bindHLSEvents(hls) {
            const Hls = hls.constructor;
            hls.on(Hls.Events.ERROR, (_event, data) => {
                console.warn(data.fatal, data.type, data.details);
                hlsErrors.push([Date.now(), data.type, data.details]);
                hlsErrorsCount++;
            });
            hls.on(Hls.Events.LEVEL_SWITCHING, (_event, data) => {
                console.warn(data);
                bitrates.push([Date.now(), data.bitrate]);
            });
            hls.on(Hls.Events.LEVEL_SWITCHED, (_event, data) => {
                console.warn(data);
                levels.push([Date.now(), data.level]);
            });
            setInterval(() => {
                latencies.push([hls.latency, Date.now()]);
            }, 3000);
        }
    }

})();

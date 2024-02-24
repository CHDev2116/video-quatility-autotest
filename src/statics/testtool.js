(function () {
    let logs = [];
    let warns = [];
    let startuptime = [];
    let waitingCount = 0;
    let seekingCount = 0;
    let warnsCount = 0;
    let latency = [];

    window.testTool = {    
        getWaitingCount() {
            return waitingCount;
        },

        getLogs() {
            return logs;
        },

        getStartupTime() {
            return startuptime;
        },

        getWarns() {
            return warns;
        },

        getWarnsCount() {
            return warnsCount;
        },

        clearWarns() {
            warns = [];
            return warns;
        },

        getSeekingCount() {
            return seekingCount;
        },

        getLatency() {
            return latency;
        },

        clearLatency() {
            latency = [];
            return latency;
        },


        bindMedia(element) {
            element.addEventListener('waiting', () => {
                console.log('waiting');
                logs.push(['waiting', Date.now()]);
                waitingCount++;
            });
            element.addEventListener('play', () => {
                console.log('play');
                startuptime.push(['play', Date.now()]);
            });
            element.addEventListener('timeupdate', () => {
                console.log('timeupdate');
                logs.push(['timeupdate', Date.now()]);
            });
            element.addEventListener('playing', () => {
                console.log('playing');
                startuptime.push(['playing', Date.now()]);
            });
            element.addEventListener('seeking', () => {
                console.log('seeking');
                logs.push(['seeking', Date.now()]);
                seekingCount++;
            });
        },

        bindHLSEvents(hls) {
            const Hls = hls.constructor;
            hls.on(Hls.Events.ERROR, (_event, data) => {
                console.warn(data.fatal, data.type, data.details);
                warns.push([Date.now(), data.type, data.details]);
                warnsCount++;
            });
            setInterval(() => {
                latency.push([hls.latency, Date.now()]);
            }, 3000);
        }
    }            

})();    
import matplotlib.pyplot as plt
import random
import schedule
import speedtest
import time

from datetime import datetime, timedelta, timezone
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Keep browser open
from selenium.webdriver.chrome.options import Options

# from reset_env import reset_env
import variables as v

# Chrome usage
chrome_options = Options()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_options.add_experimental_option("detach", True)


def run_test():
    # reset_env()
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    chrome_driver.get(
        "https://cheryl1.mlytics.co/event-listener/v6/sdk-automation-hlsjs.html?src=" + v.src + "&configURL=" + v.configURL)
    print(datetime.now())
    time.sleep(2)

    # Play
    chrome_driver.find_element(by=By.ID, value="video").click()
    time.sleep(3)

    try:
        def send_req():

            def startup_times():
                # Collect startup times
                startup_times_js = 'return testTool.getStartupTimes()'
                startup_times = chrome_driver.execute_script(startup_times_js)

                if not startup_times:
                    raise Exception('Fail to generate startup times.')
                else:
                    print(len(startup_times))

                if len(startup_times) <= 1:
                    raise Exception('Fail to generate playing_log.')
                else:
                    for _ in startup_times:
                        play = startup_times[0]
                        play_timestamp = int(play[1]) / 1000
                        play_time = datetime.fromtimestamp(play_timestamp)
                        time_1 = datetime.strptime(str(play_time), "%Y-%m-%d %H:%M:%S.%f")

                        playing = startup_times[1]
                        playing_timestamp = int(playing[1]) / 1000
                        playing_time = datetime.fromtimestamp(playing_timestamp)
                        time_2 = datetime.strptime(str(playing_time), "%Y-%m-%d %H:%M:%S.%f")

                        # Calculate startup times
                        video_startup_times = time_2 - time_1

                    def generate_startup_times():
                        file = open("results/results_for_hls.js.html", "a")
                        file.write("<h2>HLS.js automation testing results</h2>")
                        file.write("\n")
                        file.write("<p>Startup Times(seconds): </p>")
                        file.write("\n")
                        file.write(str(video_startup_times))
                        file.write("\n")
                        file.close()

                    generate_startup_times()

            startup_times()

            def set_network_connections():
                change_rate = random.random()
                if change_rate < v.possibility:
                    print(change_rate)
                    chrome_driver.set_network_conditions(
                        offline=False,
                        latency=5,
                        download_throughput=random.randint(v.min_download, v.max_download),
                        upload_throughput=v.upload)

            schedule.every(v.times).seconds.until(timedelta(seconds=v.total_time)).do(set_network_connections)

            ax = []
            ay = []
            az = []
            at = []
            ae = []

            def collect_logs():
                # Collect media events
                media_events_len_js = 'return testTool.getMediaEvents().length'
                media_events_len = chrome_driver.execute_script(media_events_len_js)
                # Collect "waiting" count
                waiting_count_js = 'return testTool.getWaitingCount()'
                waiting_count = chrome_driver.execute_script(waiting_count_js)
                # Collect HLS errors
                hls_errors_js = 'return testTool.getHlsErrors()'
                hls_errors = chrome_driver.execute_script(hls_errors_js)
                # Collect HLS errors count
                hls_errors_count_js = 'return testTool.getHlsErrorsCount()'
                hls_errors_count = chrome_driver.execute_script(hls_errors_count_js)
                # Clear HLS errors
                clear_hls_errors_js = 'return testTool.clearHlsErrors()'
                chrome_driver.execute_script(clear_hls_errors_js)
                # Collect "seeking" count
                seeking_count_js = 'return testTool.getSeekingCount()'
                seeking_count = chrome_driver.execute_script(seeking_count_js)
                # Collect latencies
                latencies_js = 'return testTool.getLatencies()'
                latencies = chrome_driver.execute_script(latencies_js)
                # Clear latencies
                clear_latencies_js = 'return testTool.clearLatencies()'
                chrome_driver.execute_script(clear_latencies_js)
                # Collect bitrates
                bitrates_js = 'return testTool.getBitrates()'
                bitrates = chrome_driver.execute_script(bitrates_js)
                # Clear bitrates
                clear_bitrates_js = 'return testTool.clearBitrates()'
                chrome_driver.execute_script(clear_bitrates_js)
                # Collect levels
                levels_js = 'return testTool.getLevels()'
                levels = chrome_driver.execute_script(levels_js)
                # Clear levels
                clear_levels_js = 'return testTool.clearLevels()'
                chrome_driver.execute_script(clear_levels_js)

                ax.append(datetime.now(timezone.utc))
                ay.append(waiting_count)
                az.append(seeking_count)
                at.append(datetime.now(timezone.utc))
                ae.append(hls_errors_count)

                hls_errors_str = ''.join(str(x) for x in hls_errors)
                latencies_str = ''.join(str(x) for x in latencies)
                bitrates_str = ''.join(str(x) for x in bitrates)
                levels_str = ''.join(str(x) for x in levels)

                def generate_figure_and_results():
                    plt.ion()
                    plt.figure(1)
                    plt.clf()
                    plt.plot(ax, ay, marker='o', linestyle='-', color='orange', label='waiting')
                    plt.plot(ax, az, marker='o', linestyle='-', color='red', label='seeking')
                    plt.legend(loc='upper left')
                    plt.xlabel('Timeline', color='blue')
                    plt.ylabel('Lag or spinning', color='red')
                    plt.title('Video quality for HLS.js', color='blue')
                    plt.xticks(rotation=-25)
                    plt.pause(0.5)
                    plt.savefig('results/video_quality_for_hls.js.png', transparent=True)

                    plt.figure(2)
                    plt.clf()
                    plt.plot(at, ae, marker='o', linestyle='-', color='red', label='Errors')
                    plt.legend(loc='upper left')
                    plt.xlabel('Timeline', color='blue')
                    plt.ylabel('HLS errors', color='red')
                    plt.title('HLS errors for HLS.js', color='blue')
                    plt.xticks(rotation=-25)
                    plt.pause(0.5)
                    plt.savefig('results/hls_errors_for_hls.js.png', transparent=True)

                    file = open("results/video_quality_for_hls.js.html", "a")
                    file.write("<div>media events length: </div>")
                    file.write("\n")
                    file.write(str(media_events_len))
                    file.write("\n")
                    file.write("<div>waiting count: </div>")
                    file.write("\n")
                    file.write(str(waiting_count))
                    file.write("\n")
                    file.write("<div>seeking count: </div>")
                    file.write("\n")
                    file.write(str(seeking_count))
                    file.write("\n")
                    file.close()

                    file = open("results/latencies_for_hls.js.html", "a")
                    file.write("<div>current latencies: </div>")
                    file.write("\n")
                    file.write(latencies_str)
                    file.write("\n")
                    file.close()

                    file = open("results/hls_errors_for_hls.js.html", "a")
                    file.write("<div>hls errors: </div>")
                    file.write("\n")
                    file.write(hls_errors_str)
                    file.write("\n")
                    file.write("<div>hls errors count: </div>")
                    file.write("\n")
                    file.write(str(hls_errors_count))
                    file.write("\n")
                    file.close()

                    file = open("results/bitrates_and_levels_for_hls.js.html", "a")
                    file.write("<div>current bitrates: </div>")
                    file.write("\n")
                    file.write(bitrates_str)
                    file.write("\n")
                    file.write("<div>current levels: </div>")
                    file.write("\n")
                    file.write(levels_str)
                    file.write("\n")
                    file.close()

                generate_figure_and_results()

            schedule.every(v.times).seconds.until(timedelta(seconds=v.total_time)).do(collect_logs)

            while True:
                schedule.run_pending()
                time.sleep(1)
                if len(schedule.get_jobs()) == 0:
                    break

            hls_js_png1_html = "<p><img src='video_quality_for_hls.js.png' alt='video quality for hls.js' /></p>"
            with open('results/results_for_hls.js.html', 'a') as f:
                f.write(hls_js_png1_html)
                f.write("\n")

            hls_js_quality_html = ("<p><a href='Video_quality_for_hls.js.html'> "
                                   "video quality for hls.js</a></p>")
            with open('results/results_for_hls.js.html', 'a') as f:
                f.write(hls_js_quality_html)
                f.write("\n")

            hls_js_png2_html = ("<p><img src='hls_errors_for_hls.js.png' alt='hls errors for hls.js' "
                                "/></p>")
            with open('results/results_for_hls.js.html', 'a') as f:
                f.write(hls_js_png2_html)
                f.write("\n")

            hls_js_hls_errors_html = ("<p><a href='hls_errors_for_hls.js.html'> "
                                      "hls errors for hls.js</a></p>")
            with open('results/results_for_hls.js.html', 'a') as f:
                f.write(hls_js_hls_errors_html)
                f.write("\n")

            hls_js_latencies_html = "<p><a href='latencies_for_hls.js.html'> latencies for hls.js</a></p>"
            with open('results/Results_for_hls.js.html', 'a') as f:
                f.write(hls_js_latencies_html)
                f.write("\n")

            hls_js_bitrates_and_levels_html = ("<p><a href='bitrates_and_levels_for_hls.js.html'> "
                                               "bitrates and levels for hls.js</a></p>")
            with open('results/results_for_hls.js.html', 'a') as f:
                f.write(hls_js_bitrates_and_levels_html)
                f.write("\n")

        send_req()

    except Exception as e:
        print(e)
        print('Pause test execution.')

    finally:
        # Run speed test
        st = speedtest.Speedtest(secure=True)
        download_speed = st.download() / 1024 / 1024
        upload_speed = st.upload() / 1024 / 1024
        file = open("results/results_for_hls.js.html", "a")
        file.write("<p>Download Speed(Mbps): </p>")
        file.write("\n")
        file.write(str(round(download_speed, 2)))
        file.write("\n")
        file.write("<p>Upload Speed(Mbps): </p>")
        file.write("\n")
        file.write(str(round(upload_speed, 2)))
        file.write("\n")
        file.close()

        # close browser
        chrome_driver.close()
        print(datetime.now())


if __name__ == '__main__':
    for i in range(1):
        run_test()
        print(i)

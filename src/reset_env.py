import os

filename1 = "results/results_for_video.js.html"
filename2 = "results/results_for_hls.js.html"
filename3 = "results/results_for_dplayer.html"
filename4 = "results/hls_errors_for_video.js.html"
filename5 = "results/hls_errors_for_hls.js.html"
filename6 = "results/hls_errors_for_dplayer.html"
filename7 = "results/latencies_for_video.js.html"
filename8 = "results/latencies_for_hls.js.html"
filename9 = "results/latencies_for_dplayer.html"
filename10 = "results/video_quality_for_video.js.png"
filename11 = "results/video_quality_for_hls.js.png"
filename12 = "results/video_quality_for_dplayer.png"
filename13 = "results/hls_errors_for_video.js.png"
filename14 = "results/hls_errors_for_hls.js.png"
filename15 = "results/hls_errors_for_dplayer.png"
filename16 = "results/video_quality_for_video.js.html"
filename17 = "results/video_quality_for_hls.js.html"
filename18 = "results/video_quality_for_dplayer.html"
filename19 = "results/bitrates_and_levels_for_video.js.html"
filename20 = "results/bitrates_and_levels_for_hls.js.html"
filename21 = "results/bitrates_and_levels_for_dplayer.html"
filename22 = "results/network_conditions_for_video.js.html"
filename23 = "results/network_conditions_for_hls.js.html"
filename24 = "results/network_conditions_for_dplayer.html"


def reset_env():
    def remove_file1_html():
        if os.path.exists(filename1):
            os.remove(filename1)
        else:
            print("results_for_video.js.html does not exist.")

    remove_file1_html()

    def remove_file2_html():
        if os.path.exists(filename2):
            os.remove(filename2)
        else:
            print("results_for_hls.js.html does not exist.")

    remove_file2_html()

    def remove_file3_html():
        if os.path.exists(filename3):
            os.remove(filename3)
        else:
            print("results_for_dplayer.html does not exist.")

    remove_file3_html()

    def remove_file4_html():
        if os.path.exists(filename4):
            os.remove(filename4)
        else:
            print("hls_errors_for_video.js.html does not exist.")

    remove_file4_html()

    def remove_file5_html():
        if os.path.exists(filename5):
            os.remove(filename5)
        else:
            print("hls_errors_for_hls.js.html does not exist.")

    remove_file5_html()

    def remove_file6_html():
        if os.path.exists(filename6):
            os.remove(filename6)
        else:
            print("hls_errors_for_dplayer.html does not exist.")

    remove_file6_html()

    def remove_file7_html():
        if os.path.exists(filename7):
            os.remove(filename7)
        else:
            print("latencies_for_video.js.html does not exist.")

    remove_file7_html()

    def remove_file8_html():
        if os.path.exists(filename8):
            os.remove(filename8)
        else:
            print("latencies_for_hls.js.html does not exist.")

    remove_file8_html()

    def remove_file9_html():
        if os.path.exists(filename9):
            os.remove(filename9)
        else:
            print("latencies_for_dplayer.html does not exist.")

    remove_file9_html()

    def remove_file10_html():
        if os.path.exists(filename10):
            os.remove(filename10)
        else:
            print("video_quality_for_video.js.png does not exist.")

    remove_file10_html()

    def remove_file11_html():
        if os.path.exists(filename11):
            os.remove(filename11)
        else:
            print("video_quality_for_hls_js.png does not exist.")

    remove_file11_html()

    def remove_file12_html():
        if os.path.exists(filename12):
            os.remove(filename12)
        else:
            print("video_quality_for_dplayer.png does not exist.")

    remove_file12_html()

    def remove_file13_html():
        if os.path.exists(filename13):
            os.remove(filename13)
        else:
            print("hls_errors_for_video.js.png does not exist.")

    remove_file13_html()

    def remove_file14_html():
        if os.path.exists(filename14):
            os.remove(filename14)
        else:
            print("hls_errors_for_hls.js.png does not exist.")

    remove_file14_html()

    def remove_file15_html():
        if os.path.exists(filename15):
            os.remove(filename15)
        else:
            print("hls_errors_for_dplayer.png does not exist.")

    remove_file15_html()

    def remove_file16_html():
        if os.path.exists(filename16):
            os.remove(filename16)
        else:
            print("video_quality_for_video.js.html does not exist.")

    remove_file16_html()

    def remove_file17_html():
        if os.path.exists(filename17):
            os.remove(filename17)
        else:
            print("video_quality_for_hls.js.html does not exist.")

    remove_file17_html()

    def remove_file18_html():
        if os.path.exists(filename18):
            os.remove(filename18)
        else:
            print("video_quality_for_dplayer.html does not exist.")

    remove_file18_html()

    def remove_file19_html():
        if os.path.exists(filename19):
            os.remove(filename19)
        else:
            print("bitrates_and_levels_for_video.js.html does not exist.")

    remove_file19_html()

    def remove_file20_html():
        if os.path.exists(filename20):
            os.remove(filename20)
        else:
            print("bitrates_and_levels_for_hls.js.html does not exist.")

    remove_file20_html()

    def remove_file21_html():
        if os.path.exists(filename21):
            os.remove(filename21)
        else:
            print("bitrates_and_levels_for_dplayer.html does not exist.")

    remove_file21_html()

    def remove_file22_html():
        if os.path.exists(filename22):
            os.remove(filename22)
        else:
            print("network_conditions_for_video.js.html does not exist.")

    remove_file22_html()

    def remove_file23_html():
        if os.path.exists(filename23):
            os.remove(filename23)
        else:
            print("network_conditions_for_hls.js.html does not exist.")

    remove_file23_html()

    def remove_file24_html():
        if os.path.exists(filename24):
            os.remove(filename24)
        else:
            print("network_conditions_for_dplayer.html does not exist.")

    remove_file24_html()


if __name__ == '__main__':
    for i in range(1):
        reset_env()
        print(i)

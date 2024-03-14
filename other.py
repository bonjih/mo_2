import pandas as pd
import matplotlib.pyplot as plt



def get_df_vals(seconds: float, fps: int, df_lst: list, sum, sma_params: dict):
    """
        fps: input video frame rate as an int
        seconds: input video timestamp
        df_list: reference output list for sma calculation
        params: parameters for sma and thresholds settings

    """
    sma = 0.0
    fps_n = sma_params["interval_seconds"] * fps - 1

    if len(df_lst) >= fps_n:
        for i in range(len(df_lst) - 1, (len(df_lst) - 1) - fps_n, -1):
            sma = sma + df_lst[i]["motion_sum"]

    sma = (sma + sum) / float(fps_n)

    df_vals = {
        "sec": seconds,
        "motion_sum": sum,
        "motion_sma": sma,
        "motion_exceeded_35": sma >= sma_params["t0"],
        # 0.2[0.0, 152974.7, 305949.4, 458924.1, 611898.8, 764873.5, 917848.2, 1070822.9000000001, 1223797.6, 1376772.3, 1529747.0]
        "motion_exceeded_50": sma >= sma_params["t1"],
        # 0.25  # [1529747.0, 1682721.7, 1835696.4, 1988671.1, 2141645.8000000003, 2294620.5, 2447595.2, 2600569.9000000004, 2753544.6, 2906519.3, 3059494.0]
    }
    return df_vals


def calc_area_percent(tl, tr, bl, C):
    """
    calculaes the percentage/area of the bounding box
    for the purpose of excluding small areas
    :param tl: bb coords top left
    :param tr: bb coords top right
    :param bl: bb coords bottom left
    :param C: bb coords bottom right
    :return: BB area percentage contours fill it
    """
    box_area = (tr[0] - tl[0]) * (bl[1] - tl[1])
    topmost = tuple(C[C[:, :, 1].argmin()][0])
    percent = 1 - ((topmost[1] - 340) / 740)
    return box_area, percent


def write_csv(intensity):
    data = {'intensity_Sum': [intensity]}
    df = pd.DataFrame(data)

    with open('intensity.csv', 'a') as csvfile:
        df.to_csv(csvfile, header=None, mode='a', index=False)


def plot_histo(csv_file):
    df = pd.read_csv(csv_file)
    plt.hist(df['intensity_Sum'], bins=5, color='blue')
    plt.grid(True)
    plt.show()


#plot_histo('intensity.csv')


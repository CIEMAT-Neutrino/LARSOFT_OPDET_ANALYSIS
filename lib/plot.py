import scipy as sc
import numpy as np
import pandas as pd
import plotly.express as px

import plotly.graph_objects as go
from scipy.optimize import curve_fit
from .fit import gauss

def gauss_fit_distribution(df,this_bin,variable,color,color_map,output_data,xlim=(1,90),acc=100,terminal=False,fig=None):
    plot_array = []; fit_labels = ["AMP", "MEAN", "STD"]
    for idx,filter in enumerate(df[color].unique()):
        filter_df = df[df[color]==filter].copy()
        perc = np.percentile(filter_df[variable], xlim)
        hist, bin_edges = np.histogram(filter_df[variable], bins=np.linspace(perc[0],perc[1],acc))
        hist = hist / np.sum(hist)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        
        try:
            popt, pcov = curve_fit(gauss, bin_centers, hist, p0=[np.max(hist),np.mean(bin_centers),0.1], bounds=([0, -1, -np.inf], [1, 1, np.inf]))
            perr = np.sqrt(np.diag(pcov))
            if terminal:
                print("Fitting "+filter+", trying with p0 = [np.max(hist),np.mean(bin_centers),0.1]")
                print("----------------"+filter+"----------------")
                for i in range(len(popt)):
                    print(fit_labels[i]+'\t= %.2E\t± %.2E' % (popt[i], perr[i]))
                print("-------------------------------------")
        except:
            print("Fit failed for "+filter)
            popt = [0,0,0]
            perr = [0,0,0]
            
        fit = gauss(bin_centers, *popt)
        fit_data = {"FILTER": filter,
                    # "fit": fit, 
                    # "bin_centers": bin_centers, 
                    "THIS_PE": this_bin, 
                    "AMP": popt[0], "AMP_ERR": perr[0], 
                    "MEAN": popt[1],"MEAN_ERR": perr[1], 
                    "STD": popt[2], "STD_ERR": perr[2]
                    }
        output_data.append(fit_data)
        plot_dict = {"FILTER": filter, "HIST":hist, "BIN":bin_centers, "FIT": fit}
        plot_array.append(plot_dict)

    try:
        plot_df = pd.DataFrame(plot_array).explode(["HIST","BIN","FIT"])
        fig = px.bar(plot_df,
                    x="BIN",
                    y="HIST", 
                    color="FILTER", 
                    color_discrete_sequence=pd.Series(plot_df["FILTER"].unique()).map(color_map),
                    barmode="overlay", 
                    template="presentation",
                    )
        for idx,filter in enumerate(df[color].unique()):
            fig.add_trace(go.Scatter(name="FIT "+filter,x=plot_df[plot_df["FILTER"] == filter]["BIN"], y=plot_df[plot_df["FILTER"] == filter]["FIT"],line=dict(color=color_map[filter])))
            # fig.add_vline(x=np.mean(df[df[color] == filter][variable]))
    except:
        fig = plt.figure(figsize=(10,5))
        for plot in plot_array:
            plt.bar(plot["BIN"], plot["HIST"], color=color_map[plot["FILTER"]])
            plt.plot(plot["BIN"], plot["FIT"], label=plot["FILTER"], color=color_map[plot["FILTER"]])
        plt.ylabel("Counts"); plt.xlabel(variable)
        plt.grid()
        plt.legend()
        # plt.show()

    return fig,output_data

def get_gauss_fit_data(df,true,true_lim,variable,color,color_map,xlim=(1,90),acc=100,terminal=False,fig=None):
    pe_bins = true_lim
    pe_bin_centers = (pe_bins[1:]+pe_bins[:-1])/2
    data = []
    fig_list = []
    for idx,this_bin in enumerate(pe_bin_centers):
        this_df = df[(df[true] > pe_bins[idx])*(df[true] < pe_bins[idx+1])]
        fig,data = gauss_fit_distribution(this_df,this_bin,variable,color,color_map,data,xlim=xlim,acc=acc,terminal=terminal,fig=fig)
        fig.update_layout(bargap = 0)
        fig_list.append(fig)
    return fig_list,data
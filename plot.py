import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__=="__main__":
    df = pd.read_pickle('/home/ec2-user/MentaLLama/MentalLLaMA/quality_evaluation_results/bart_score_output.pkl')
    result_bart = pd.DataFrame()
    temp_bart = pd.DataFrame()
    result_bart['dataset name'] = df.keys()
    result_bart['BART score'] = df.values()
    result_bart['model name'] = 'mistral_7b_finetuned'
    temp_bart['dataset name'] = df.keys()
    temp_bart['BART score'] = [-2.90,-2.5,-3.25,-3.27,-3.26]
    temp_bart['model name'] = 'mentalLLaMA_7b_chat'
    result_bart = pd.concat([result_bart,temp_bart],axis=0)
    ### plot ##
    # plt.style.use("seaborn")
    # plt.rcParams["figure.figsize"] = (20,7)
    # plt.plot(x=result_bart['bart_score'],y=result_bart['dataset'])
    # plt.savefig('/home/ec2-user/MentaLLama/MentalLLaMA/src/BARTScore/bart_score_plot.png', bbox_inches='tight')
    # plt.show()
    line_plot = sns.lineplot(y=result_bart['BART score'],x=result_bart['dataset name'],hue=result_bart['model name'])
    fig = line_plot.get_figure()
    fig.savefig("/home/ec2-user/MentaLLama/MentalLLaMA/src/BARTScore/bart_score_plot.png") 
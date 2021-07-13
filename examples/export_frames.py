import plotly.graph_objects as go

def export_frames(fig, name):
    sequence = []

    #im = Image.open(....)

    # im is your original image
    for i, frame in enumerate(fig.frames):
        frame_fig = go.Figure(fig.frames[i].data, fig.layout)
        frame_fig.write_image("images/image" + str(i) + ".svg")


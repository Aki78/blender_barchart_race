import plotly.graph_objects as go

def export_frames(fig, name, type="svg"):
    sequence = []

    #im = Image.open(....)

    # im is your original image
    for i, frame in enumerate(fig.frames):
        frame_fig = go.Figure(fig.frames[i].data, fig.layout)
        if type="json":
            frame_fig.write_json("jsons/" + name + str(i) + "." + "json")
        else:
            frame_fig.write_image("images/" + name + str(i) + "." + type, pretty=True)


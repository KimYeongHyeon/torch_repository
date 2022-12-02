def get_output_shape(model, image_dim):
    return model(torch.rand(*(image_dim))).data.shape

import torch
import torchvision

device = 'cpu'

def mobilenetV2():
    model = torchvision.models.get_model('mobilenet_v2', weights=None)
    model.classifier[1] = torch.nn.Linear(in_features=model.classifier[1].in_features, out_features=14)
    model.load_state_dict(torch.load('./model/model.pth',map_location=torch.device('cpu')))
    model = model.to(device)
    return model

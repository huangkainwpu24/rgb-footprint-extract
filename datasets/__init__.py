from .CrowdAIDataset import CrowdAIDataset
from .Urban3dDataset import Urban3dDataset
from .SpaceNetDataset import SpaceNetDataset
from .CombinedDataset import CombinedDataset
import os


def build_dataloader(dataset, data_root, boundary_ks, transforms, resize=2048, split=2):
    if dataset == "urban3d":
        train =  Urban3dDataset(
            os.path.join(data_root, "Urban3D/train"), 
            boundary_kernel_size=boundary_ks, 
            transforms=transforms,
            resize=resize, split=split
        )
        val = Urban3dDataset(
            os.path.join(data_root, "Urban3D/val"), 
            boundary_kernel_size=boundary_ks, 
            transforms=transforms,
            resize=resize, split=split
        )
    elif dataset == "spaceNet":
        train = SpaceNetDataset(os.path.join(data_root, "SpaceNet/Vegas/train"), boundary_ks, transforms)
        val = SpaceNetDataset(os.path.join(data_root, "SpaceNet/Vegas/val"), boundary_ks, transforms)
    elif dataset == "crowdAI":
        train = CrowdAIDataset(os.path.join(data_root, "AICrowd/train"), boundary_ks, transforms, data_slice=None)
        val = CrowdAIDataset(os.path.join(data_root, "AICrowd/val"), boundary_ks, transforms, data_slice=None)
    elif dataset == "combined":
        train = CombinedDataset(data_root, boundary=(boundary_ks is not None))
        val = CombinedDataset(data_root, boundary=(boundary_ks is not None), train=False)
    else:
        raise NotImplementedError()

    return train, val

def build_test_dataloader(dataset, data_root, transforms):
    if dataset == "urban3d":
        return Urban3dDataset(os.path.join(data_root, "Urban3D/test"), boundary_kernel_size=None, transforms=transforms)
    elif dataset == "spaceNet":
        return SpaceNetDataset(os.path.join(data_root, "SpaceNet/Vegas/test"), None, transforms)
    elif dataset == "crowdAI":
        return CrowdAIDataset(os.path.join(data_root, "AICrowd/test"), None, transforms)
    else:
        raise NotImplementedError()
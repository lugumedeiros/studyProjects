% Train Imds
filename = "myTrainData";
imdsASL = imageDatastore(filename,"IncludeSubfolders", true,"LabelSource", "foldernames");

[imdsTrain, imdsValid] = splitEachLabel(imdsASL,0.8,"randomized");
augTrain = augmentedImageDatastore([224, 224], imdsTrain);
augValid = augmentedImageDatastore([224, 224], imdsValid);
opts = trainingOptions("adam","ValidationData",augValid,"Shuffle","every-epoch","Plots","training-progress", "ValidationFrequency",15);

% Test imds
filenameTest = "myTestData";
imdsASLTest = imageDatastore(filenameTest,"IncludeSubfolders", true,"LabelSource", "foldernames");
augTest = augmentedImageDatastore([224, 224], imdsASLTest);

%   Transfer learning with rez50
%   This test gave me ~91% accuracy
%   It took me 45 min to train but it reached plato at ~25min and I forgot to
% increase validation frequency.
net_rez50ASL = trainNetwork(augTrain, lgraph_1, opts);
rez50ALS_results = classify(net_rez50ASL, augTest);
testAccuracy = nnz(rez50ALS_results == imdsASLTest.Labels)/length(rez50ALS_results);
confusionchart(imdsASLTest.Labels,rez50ALS_results);

%   Simple empty model from zero.
%   This time validation frequency was on 15
%   This test gave me ~31% of accuracy and took 8 min.
%   I believe it has the same problem as the other test, test data is
% too similar to train data...
%   
simple_layers = [
    imageInputLayer([224 224 3],"Name","imageinput")
    convolution2dLayer([3 3],32,"Name","conv","Padding","same")
    reluLayer("Name","relu")
    maxPooling2dLayer([5 5],"Name","maxpool","Padding","same")
    fullyConnectedLayer(24,"Name","fc")
    softmaxLayer("Name","softmax")
    classificationLayer("Name","classoutput")];

simple_net = trainNetwork(augTrain, simple_layers, opts);
simple_result = classify(simple_net, augTest);
simple_testAccuracy = nnz(simple_result == imdsASLTest.Labels)/length(simple_result);
confusionchart(imdsASLTest.Labels,simple_result);
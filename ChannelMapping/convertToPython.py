import h5py
import sys
import numpy as np

def convert_to_ndarray():
    fileName = sys.argv[0] #get the filename from command line arguments

    f = h5py.File(fileName) #open a file pointer to point to the .mat file

    #extract the data from rawData via f, location and channel data into respective ndarrays
    channel_data = np.array(f.get('rawData/channel'))
    user_loc_data = np.array(f.get('rawData/userLoc'))

    ''' Normalization
    1. Take abs value of channel_data and user_loc_data. 
    For complex values abs is defined as - sqrt(real^2 + imag^2)
    For real values - if val < 0, -val else val

    2. Find the max value for channel data and loc data. 
    Divide the enitre dataset with it to get the values in [-1, 1]
    
    '''
    print('Normalizing the absolute of the channel data')

    channel_data = np.abs(channel_data['real']+channel_data['imag']*1j)
    #channel_data = np.abs(np.abs(channel_data.view('complex')))
    max_channel_data = np.amax(channel_data)
    channel_data = channel_data / max_channel_data

    print('Normalizing the absolute of the userLoc data')

    user_loc_data = np.abs(user_loc_data)
    max_user_loc_data = np.amax(user_loc_data)
    user_loc_data = user_loc_data / max_user_loc_data

    return 










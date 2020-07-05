import numpy as np
import matplotlib.pyplot as plt
import pyroomacoustics as pra

corners = np.array([[0,0], [0,3], [5,3], [5,1], [5,0]]).T  # [x,y]
room = pra.Room.from_corners(corners)
room = pra.Room.from_corners(corners)
room.extrude(2.)

fig, ax = room.plot()
ax.set_xlim([0, 5])
ax.set_ylim([0, 3])
ax.set_zlim([0, 2]);
room.plot()
"""# Create a 4 by 6 metres shoe box room
room = pra.ShoeBox([4,6])

# Add a source somewhere in the room
room.add_source([2.5, 4.5])

# Create a linear array beamformer with 4 microphones
# with angle 0 degrees and inter mic distance 10 cm
R = pra.linear_2D_array([2, 1.5], 4, 0, 0.1)
room.add_microphone_array(pra.Beamformer(R, room.fs))

# Now compute the delay and sum weights for the beamformer
room.mic_array.rake_delay_and_sum_weights(room.sources[0][:1])

# plot the room and resulting beamformer
room.plot(freq=[1000, 2000, 4000, 8000], img_order=0)
plt.show()"""
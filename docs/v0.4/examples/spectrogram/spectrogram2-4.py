plot = specgram.plot(norm='log', cmap='viridis')
ax = plot.gca()
ax.set_ylim(0, 500)
ax.set_title('LIGO-Hanford strain data around GW150914')
ax.set_epoch(1126259462.427)
ax.set_xlim(1126259462.427-.5, 1126259462.427+.5)
plot.show()
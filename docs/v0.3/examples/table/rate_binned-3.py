plot = rates.plot(label='name')
plot.set_xlim(968654552, 968654562)
plot.set_ylabel('Event rate [Hz]')
plot.set_title('LIGO Hanford Observatory event rate for GW100916')
plot.add_legend()
plot.show()
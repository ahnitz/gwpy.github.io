plot = events.hist('snr', weights=1/10., log=True, logbins=True, histtype='stepfilled', cumulative=-1)
plot.set_xlabel('Signal-to-noise ratio (SNR)')
plot.set_ylabel('Rate [Hz]')
plot.set_title('LHO event triggers for GW100916')
plot.show()
import java.util.logging.Logger;

public class AudioAdapter implements AudioPlayer {

    private static final Logger logger = Logger.getLogger(AudioAdapter.class.getName());
    private MP3Player mp3Player;
    private WAVPlayer wavPlayer;

    public AudioAdapter(MP3Player mp3Player, WAVPlayer wavPlayer) {
        this.mp3Player = mp3Player;
        this.wavPlayer = wavPlayer;
    }

    @Override
    public void play(String filename) {
        if (filename.endsWith(".mp3")) {
            logger.info("Adaptando archivo MP3 a WAV...");
            wavPlayer.play(filename.replace(".mp3", ".wav")); // Simulación de conversión
        } else if (filename.endsWith(".wav")) {
            logger.info("Adaptando archivo WAV a MP3...");
            mp3Player.play(filename.replace(".wav", ".mp3")); // Simulación de conversión
        } else {
            logger.warning("Formato no compatible");
        }
    }
}

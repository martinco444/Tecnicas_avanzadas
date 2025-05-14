import java.util.logging.Logger;

public class WAVPlayer implements AudioPlayer {

    private static final Logger logger = Logger.getLogger(WAVPlayer.class.getName());

    @Override
    public void play(String filename) {
        if (filename.endsWith(".wav")) {
            logger.info("Reproduciendo archivo WAV: " + filename);
        } else {
            logger.warning("Formato no compatible para WAVPlayer");
        }
    }
}

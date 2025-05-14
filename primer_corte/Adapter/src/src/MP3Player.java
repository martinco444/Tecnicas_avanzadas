import java.util.logging.Logger;

public class MP3Player implements AudioPlayer {

    private static final Logger logger = Logger.getLogger(MP3Player.class.getName());

    @Override
    public void play(String filename) {
        if (filename.endsWith(".mp3")) {
            logger.info("Reproduciendo archivo MP3: " + filename);
        } else {
            logger.warning("Formato no compatible para MP3Player");
        }
    }
}

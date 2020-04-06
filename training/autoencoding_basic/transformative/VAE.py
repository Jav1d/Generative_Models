
import tensorflow as tf
from training.autoencoding_basic.autoencoders.VAE import VAE

class VAE(VAE):
    # batch_size =  batch_size * Episode_Len
    def batch_cast(self, xt0, xt1):
        xt0 = tf.cast(xt0, dtype=tf.float32)/self.input_scale
        xt1 = tf.cast(xt1, dtype=tf.float32) / self.input_scale
        return {
                   'inference_logvariance_inputs': xt0,
                   'inference_mean_inputs': xt0
               }, \
               {
                   'x_logits': xt1,
                   'z_latents': 0.0,
                   'x_logpdf':0.0,
                   'x_logvariance': 0.0,
                   'x_mean': 0.0
               }
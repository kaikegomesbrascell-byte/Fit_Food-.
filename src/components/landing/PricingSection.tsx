import { Button } from "@/components/ui/button";
import { Check, ArrowRight } from "lucide-react";
import { motion } from "framer-motion";
import { useState } from "react";
import { CheckoutModal } from "@/components/CheckoutModal";

const benefits = [
  "Extração ilimitada de leads",
  "Exportação CSV e Excel",
  "Validação de emails e telefones",
  "Múltiplas fontes de dados",
  "Atualizações gratuitas vitalícias",
  "Suporte via email",
];

const ease = [0.16, 1, 0.3, 1] as const;

const PricingSection = () => {
  const [checkoutOpen, setCheckoutOpen] = useState(false);

  return (
    <section id="pricing" className="border-t border-border bg-card px-6 py-24 md:py-32">
      <CheckoutModal open={checkoutOpen} onOpenChange={setCheckoutOpen} />
      <div className="mx-auto max-w-2xl text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.7, ease }}
        >
          <span className="font-mono-data text-xs font-medium uppercase tracking-widest text-accent">Preço</span>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
            Pagamento único. Acesso vitalício.
          </h2>
          <p className="mt-4 text-muted-foreground">
            Sem assinaturas, sem taxas mensais. Pague uma vez e tenha acesso completo ao extrator.
          </p>
        </motion.div>

        <motion.div
          className="mt-12 rounded-lg border-2 border-accent/40 bg-background p-8 shadow-lg"
          initial={{ opacity: 0, y: 30, scale: 0.97 }}
          whileInView={{ opacity: 1, y: 0, scale: 1 }}
          viewport={{ once: true, amount: 0.2 }}
          transition={{ duration: 0.8, ease, delay: 0.15 }}
        >
          <div className="mb-6">
            <span className="font-mono-data text-xs font-medium uppercase tracking-widest text-accent">Licença Completa</span>
            <div className="mt-3 flex items-baseline justify-center gap-1">
              <motion.span
                className="text-5xl font-extrabold tracking-tight text-foreground"
                initial={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, ease, delay: 0.3 }}
              >
                R$ 297
              </motion.span>
              <span className="text-muted-foreground">,00</span>
            </div>
            <p className="mt-1 text-sm text-muted-foreground">pagamento único</p>
          </div>

          <ul className="mb-8 space-y-3 text-left">
            {benefits.map((benefit, i) => (
              <motion.li
                key={benefit}
                className="flex items-center gap-3 text-sm text-foreground"
                initial={{ opacity: 0, x: -12 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, ease, delay: 0.35 + i * 0.06 }}
              >
                <Check className="h-4 w-4 shrink-0 text-accent" />
                {benefit}
              </motion.li>
            ))}
          </ul>

          <Button variant="hero" size="xl" className="w-full gap-2" onClick={() => setCheckoutOpen(true)}>
            Comprar Agora
            <ArrowRight className="h-5 w-5" />
          </Button>

          <p className="mt-4 text-xs text-muted-foreground">
            Pagamento seguro via cartão de crédito ou PIX
          </p>
        </motion.div>
      </div>
    </section>
  );
};

export default PricingSection;

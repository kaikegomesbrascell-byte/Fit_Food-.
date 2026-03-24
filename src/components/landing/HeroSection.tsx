import { Button } from "@/components/ui/button";
import { Download, ArrowRight } from "lucide-react";
import { motion } from "framer-motion";
import { useState } from "react";
import LeadTablePreview from "./LeadTablePreview";
import { CheckoutModal } from "@/components/CheckoutModal";
import heroImage from "@/assets/hero-data-visual.jpg";

const ease = [0.16, 1, 0.3, 1];

const HeroSection = () => {
  const [checkoutOpen, setCheckoutOpen] = useState(false);

  return (
    <section className="relative overflow-hidden px-6 pb-24 pt-16 md:pt-24 md:pb-32">
      {/* Background image strip */}
      <motion.div
        className="absolute inset-x-0 top-0 h-[400px] overflow-hidden"
        initial={{ opacity: 0 }}
        animate={{ opacity: 0.2 }}
        transition={{ duration: 1.2, ease }}
      >
        <img src={heroImage} alt="" className="h-full w-full object-cover" loading="eager" />
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-background/60 to-background" />
      </motion.div>

      <div className="relative mx-auto max-w-6xl">
        <CheckoutModal open={checkoutOpen} onOpenChange={setCheckoutOpen} />
        <div className="mb-12 max-w-3xl md:mb-16">
          <motion.div
            className="mb-4"
            initial={{ opacity: 0, y: 16, filter: "blur(4px)" }}
            animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
            transition={{ duration: 0.7, ease }}
          >
            <span className="font-mono-data inline-flex items-center gap-2 rounded-full border border-accent/30 bg-accent/10 px-3 py-1 text-xs font-medium uppercase tracking-widest text-accent">
              <Download className="h-3 w-3" />
              Ferramenta de extração
            </span>
          </motion.div>

          <motion.h1
            className="text-balance text-4xl font-extrabold leading-[1.05] tracking-tight text-foreground sm:text-5xl md:text-6xl lg:text-7xl"
            initial={{ opacity: 0, y: 24, filter: "blur(6px)" }}
            animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
            transition={{ duration: 0.8, ease, delay: 0.1 }}
          >
            Extração de leads em alta velocidade.
          </motion.h1>

          <motion.p
            className="mt-6 max-w-xl text-lg leading-relaxed text-muted-foreground"
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, ease, delay: 0.25 }}
          >
            Extraia milhares de contatos qualificados em segundos. Nomes, emails, telefones e empresas — tudo pronto para importar no seu CRM.
          </motion.p>

          <motion.div
            className="mt-8 flex flex-col gap-3 sm:flex-row"
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, ease, delay: 0.35 }}
          >
            <Button variant="hero" size="xl" className="gap-2" onClick={() => setCheckoutOpen(true)}>
              Adquirir Extrator
              <ArrowRight className="h-5 w-5" />
            </Button>
            <Button variant="heroOutline" size="xl" asChild>
              <a href="#how-it-works">Como Funciona</a>
            </Button>
          </motion.div>

          <motion.div
            className="mt-8 flex items-center gap-6"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.6, delay: 0.5 }}
          >
            {[
              { value: "2.847+", label: "leads por extração" },
              { value: "12s", label: "tempo médio" },
              { value: "CSV", label: "exportação direta" },
            ].map((stat, i) => (
              <motion.div
                key={stat.value}
                className="flex flex-col"
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, ease, delay: 0.55 + i * 0.1 }}
              >
                <span className="font-mono-data text-2xl font-bold text-foreground">{stat.value}</span>
                <span className="text-xs text-muted-foreground">{stat.label}</span>
                {i < 2 && <div className="hidden" />}
              </motion.div>
            )).reduce<React.ReactNode[]>((acc, el, i) => {
              if (i > 0) acc.push(<div key={`sep-${i}`} className="h-8 w-px bg-border" />);
              acc.push(el);
              return acc;
            }, [])}
          </motion.div>
        </div>

        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.9, ease, delay: 0.5 }}
        >
          <LeadTablePreview />
        </motion.div>
      </div>
    </section>
  );
};

export default HeroSection;

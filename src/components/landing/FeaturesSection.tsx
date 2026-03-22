import { Database, Zap, Shield, FileSpreadsheet, Globe, RefreshCw } from "lucide-react";
import { motion } from "framer-motion";
import featuresBg from "@/assets/features-bg.jpg";

const features = [
  { icon: Zap, title: "Extração Ultrarrápida", description: "Processe milhares de registros em segundos com nosso motor de extração otimizado." },
  { icon: Database, title: "Dados Completos", description: "Nome, email, telefone, empresa e cargo — todos os campos que sua equipe precisa." },
  { icon: FileSpreadsheet, title: "Exportação CSV/Excel", description: "Arquivo pronto para importar no seu CRM, planilha ou ferramenta de automação." },
  { icon: Globe, title: "Múltiplas Fontes", description: "Extraia leads de diversas plataformas e diretórios online automaticamente." },
  { icon: Shield, title: "Dados Verificados", description: "Validação automática de emails e telefones para garantir qualidade dos contatos." },
  { icon: RefreshCw, title: "Atualizações Incluídas", description: "Receba todas as atualizações futuras da ferramenta sem custo adicional." },
];

const ease = [0.16, 1, 0.3, 1] as const;

const FeaturesSection = () => {
  return (
    <section id="features" className="relative border-t border-border bg-card px-6 py-24 md:py-32 overflow-hidden">
      <div className="absolute right-0 top-0 h-full w-1/2 opacity-[0.04] pointer-events-none">
        <img src={featuresBg} alt="" className="h-full w-full object-cover" loading="lazy" />
      </div>

      <div className="relative mx-auto max-w-6xl">
        <motion.div
          className="mb-16 max-w-xl"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.7, ease }}
        >
          <span className="font-mono-data text-xs font-medium uppercase tracking-widest text-accent">Recursos</span>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
            Tudo que você precisa para gerar leads qualificados.
          </h2>
        </motion.div>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((feature, i) => (
            <motion.div
              key={feature.title}
              className="group rounded-lg border border-border bg-background p-6 transition-all duration-300 hover:border-accent/40 hover:shadow-md hover:-translate-y-1"
              initial={{ opacity: 0, y: 24, filter: "blur(4px)" }}
              whileInView={{ opacity: 1, y: 0, filter: "blur(0px)" }}
              viewport={{ once: true, amount: 0.2 }}
              transition={{ duration: 0.6, ease, delay: i * 0.08 }}
            >
              <div className="mb-4 flex h-10 w-10 items-center justify-center rounded-md bg-accent/10 text-accent transition-colors group-hover:bg-accent/20">
                <feature.icon className="h-5 w-5" />
              </div>
              <h3 className="mb-2 text-lg font-semibold text-foreground">{feature.title}</h3>
              <p className="text-sm leading-relaxed text-muted-foreground">{feature.description}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FeaturesSection;

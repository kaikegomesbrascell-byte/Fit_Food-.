import Navbar from "@/components/landing/Navbar";
import HeroSection from "@/components/landing/HeroSection";
import SmartIntervalsSection from "@/components/landing/SmartIntervalsSection";
import FeaturesSection from "@/components/landing/FeaturesSection";
import HowItWorksSection from "@/components/landing/HowItWorksSection";
import LeadsExampleSection from "@/components/landing/LeadsExampleSection";
import PricingSection from "@/components/landing/PricingSection";
import BonusSection from "@/components/landing/BonusSection";
import GuaranteeSection from "@/components/landing/GuaranteeSection";
import FAQSection from "@/components/landing/FAQSection";
import FooterCTA from "@/components/landing/FooterCTA";

const Index = () => {
  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      <HeroSection />
      <SmartIntervalsSection />
      <FeaturesSection />
      <HowItWorksSection />
      <LeadsExampleSection />
      <PricingSection />
      <BonusSection />
      <GuaranteeSection />
      <FAQSection />
      <FooterCTA />
    </div>
  );
};

export default Index;

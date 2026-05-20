export type Agent = {
  id: string;
  name: string;
  role: string;
};

export type Business = {
  id: string;
  name: string;
  business_type: string;
  purpose: string;
  goals: string[];
  brand_voice: string;
};

export type Department = {
  id: string;
  business_id: string;
  name: string;
  purpose: string;
};

export type Project = {
  id: string;
  business_id?: string;
  name: string;
  goal: string;
  status: string;
  progress: number;
};

export type Task = {
  id: string;
  business_id?: string;
  project_id?: string;
  title: string;
  description: string;
  status: string;
  priority: string;
  progress: number;
};

export type Persona = {
  id: string;
  name: string;
  tone: string;
  rules: string[];
};

export type Skill = {
  id: string;
  name: string;
  skill_type: string;
  instructions: string;
  tools: string[];
};

export type LoRAProfile = {
  id: string;
  name: string;
  lora_type: string;
  base_model: string;
  trigger_phrase: string;
  strength: number;
};

export type MemoryPolicy = {
  id: string;
  name: string;
  scopes: string[];
  retrieval_limit: number;
};
